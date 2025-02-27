from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            c[Counter(s.lower())] += 1
    for v in c.values():
        if v > 1:
            c[v] += 1
    return max(c.values()) <= 98