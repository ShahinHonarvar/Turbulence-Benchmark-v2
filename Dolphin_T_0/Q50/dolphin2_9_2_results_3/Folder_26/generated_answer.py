from collections import Counter

def if_contains_anagrams(l):
    c = Counter((s.lower() for s in l if len(s) >= 3))
    return sum((v * (v - 1) // 2 for v in c.values())) >= 49