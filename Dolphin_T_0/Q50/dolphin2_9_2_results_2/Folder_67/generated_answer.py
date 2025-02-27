from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for w in lst:
        if len(w) >= 3:
            c[w.lower()] = c.get(w.lower(), 0) + 1
    pairs = 0
    for v in c.values():
        pairs += v * (v - 1) // 2
    return pairs >= 41