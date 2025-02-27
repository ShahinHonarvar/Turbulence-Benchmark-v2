from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    count = 0
    for v in c.values():
        count += v * (v - 1) // 2
    return count <= 6