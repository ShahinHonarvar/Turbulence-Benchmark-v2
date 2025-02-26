def if_contains_anagrams(lst):

    def is_valid_string(s):
        return all((c.isalpha() for c in s))

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_strings = [s for s in lst if is_valid_string(s) and len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if is_anagram(valid_strings[i], valid_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 255:
                    return False
    return True