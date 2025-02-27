from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for w in lst:
        w = ''.join(sorted(w.lower()))
        c[w] += 1
    count = sum((1 for v in c.values() if v >= 2))
    return count <= 14