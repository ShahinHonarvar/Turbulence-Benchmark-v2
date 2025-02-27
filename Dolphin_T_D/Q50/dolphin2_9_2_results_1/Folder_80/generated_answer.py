from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(s.lower())) for s in lst if len(set(s)) >= 3 and len(s) >= 3))
    pairs = {k: v * (v - 1) // 2 for k, v in c.items()}
    return sum(pairs.values()) >= 19