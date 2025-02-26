from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    valid_strings = [s.lower() for s in string_list if len(s) >= 3 and s.isalpha()]
    for str1, str2 in combinations(valid_strings, 2):
        if sorted(str1) == sorted(str2):
            anagram_count += 1
            if anagram_count > 392:
                return False
    return True