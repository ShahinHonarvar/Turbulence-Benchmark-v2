from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_cleaned = ''.join(filter(str.isalpha, s1.lower()))
        s2_cleaned = ''.join(filter(str.isalpha, s2.lower()))
        if len(s1_cleaned) >= 3 and len(s2_cleaned) >= 3:
            if sorted(s1_cleaned) == sorted(s2_cleaned):
                anagram_count += 1
        if anagram_count > 464:
            return False
    return True