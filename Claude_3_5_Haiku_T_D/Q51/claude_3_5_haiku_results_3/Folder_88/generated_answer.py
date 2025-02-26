def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_length(s):
        return len(s) >= 3
    filtered_strings = [s for s in strings if is_valid_length(s)]
    anagram_pairs = 0
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if is_anagram(filtered_strings[i], filtered_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 407:
                    return False
    return True