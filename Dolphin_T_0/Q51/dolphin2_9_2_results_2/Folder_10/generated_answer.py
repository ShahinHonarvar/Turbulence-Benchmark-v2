from collections import Counter

def if_contains_anagrams(l):
    asc = lambda s: ''.join(sorted(s))
    res = Counter((asc(x) for x in l if len(x) >= 3 and x.isalpha()))
    return sum([1 for c in res.values() if c > 1]) <= 21