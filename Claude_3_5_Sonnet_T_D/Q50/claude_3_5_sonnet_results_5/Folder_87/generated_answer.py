from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        if len(s1) >= 3 and len(s2) >= 3:
            if sorted(s1.lower()) == sorted(s2.lower()):
                anagram_count += 1
                if anagram_count >= 88:
                    return True
    return False