from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())):
            anagram_count += 1
    return anagram_count >= 41