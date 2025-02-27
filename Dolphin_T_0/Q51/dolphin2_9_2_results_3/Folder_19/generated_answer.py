from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    res = [v for v in c.values() if v > 1]
    return len(res) <= 69