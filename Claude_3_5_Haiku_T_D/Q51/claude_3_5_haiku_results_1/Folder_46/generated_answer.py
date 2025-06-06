def if_contains_anagrams(strings):

    def is_valid_string(s):
        return len(s) >= 3 and all((c.isalpha() for c in s))

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_strings = [s for s in strings if is_valid_string(s)]
    anagram_pairs = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if is_anagram(valid_strings[i], valid_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 61:
                    return False
    return True