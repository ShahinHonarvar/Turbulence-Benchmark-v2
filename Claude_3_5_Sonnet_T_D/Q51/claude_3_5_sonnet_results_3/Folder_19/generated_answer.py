from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    valid_strings = [s for s in string_list if len(s) >= 3 and s.isalpha()]
    for s1, s2 in combinations(valid_strings, 2):
        if is_anagram(s1, s2):
            anagram_count += 1
            if anagram_count > 69:
                return False
    return True