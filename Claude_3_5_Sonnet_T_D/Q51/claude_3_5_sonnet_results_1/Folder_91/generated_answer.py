from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_string(s):
        return len(s) >= 3 and s.isalpha()
    valid_strings = [s for s in string_list if is_valid_string(s)]
    anagram_count = 0
    for s1, s2 in combinations(valid_strings, 2):
        if is_anagram(s1, s2):
            anagram_count += 1
            if anagram_count > 88:
                return False
    return True