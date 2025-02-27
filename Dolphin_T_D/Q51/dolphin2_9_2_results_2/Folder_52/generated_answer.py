from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    m = {}
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            c[tuple(sorted(s))] += 1
    for key in c:
        if c[key] > 1:
            if len(m) < 43:
                m[key] = c[key]
            else:
                return False
    return len(m) <= 43