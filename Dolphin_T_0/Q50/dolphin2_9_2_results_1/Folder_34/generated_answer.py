from collections import Counter

def if_contains_anagrams(strings):
    pairs = 0
    for s1 in strings:
        for s2 in strings:
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())) and (s1 != s2):
                pairs += 1
    return pairs >= 25