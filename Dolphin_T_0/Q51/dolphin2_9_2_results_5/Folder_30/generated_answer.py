from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            c[s] += 1
    count = 0
    for v in c.values():
        count += v * (v - 1) // 2
    return count <= 28