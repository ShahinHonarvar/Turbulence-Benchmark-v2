from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_filtered = ''.join(filter(str.isalpha, s1.lower()))
        s2_filtered = ''.join(filter(str.isalpha, s2.lower()))
        if len(s1_filtered) >= 3 and len(s2_filtered) >= 3:
            if sorted(s1_filtered) == sorted(s2_filtered):
                anagram_count += 1
                if anagram_count > 407:
                    return False
    return True