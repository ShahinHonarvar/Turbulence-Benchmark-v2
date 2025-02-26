def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_length(s):
        return len(s) >= 3
    valid_strings = [s for s in string_list if is_valid_length(s)]
    anagram_pairs = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if is_anagram(valid_strings[i], valid_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 66:
                    return False
    return True