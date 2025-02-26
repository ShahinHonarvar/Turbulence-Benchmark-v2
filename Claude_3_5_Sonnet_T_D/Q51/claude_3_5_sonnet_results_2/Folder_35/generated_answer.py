from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3 and s.isalpha()]
    for s1, s2 in combinations(processed_strings, 2):
        if s1 == s2:
            anagram_count += 1
            if anagram_count > 210:
                return False
    return True