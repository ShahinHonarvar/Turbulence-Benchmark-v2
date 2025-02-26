from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    valid_strings = [s.lower() for s in string_list if len(s) >= 3 and s.isalpha()]
    for s1, s2 in combinations(valid_strings, 2):
        if sorted(s1) == sorted(s2):
            anagram_count += 1
            if anagram_count > 188:
                return False
    return True