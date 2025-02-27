from collections import Counter

def if_contains_anagrams(lst):
    ctr = Counter((c for s in lst if len(s) >= 3 for c in s.lower() if c.isalpha()))
    return sum((v >= 2 for v in ctr.values())) <= 2