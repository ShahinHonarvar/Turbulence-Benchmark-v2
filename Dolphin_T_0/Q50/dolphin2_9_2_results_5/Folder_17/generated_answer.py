from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(s.lower())) for s in lst if len(s) >= 3))
    pairs = 0
    for v in c.values():
        pairs += v * (v - 1) // 2
    return pairs >= 97