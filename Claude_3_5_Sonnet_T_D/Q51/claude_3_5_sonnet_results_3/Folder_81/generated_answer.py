from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_clean = ''.join(filter(str.isalpha, s1.lower()))
        s2_clean = ''.join(filter(str.isalpha, s2.lower()))
        if len(s1_clean) >= 3 and len(s2_clean) >= 3:
            if sorted(s1_clean) == sorted(s2_clean):
                anagram_count += 1
                if anagram_count > 79:
                    return False
    return True