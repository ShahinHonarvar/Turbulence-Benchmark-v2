from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    c = Counter()
    for w in lst:
        if len(w) >= 3:
            c[tuple(sorted(w.lower()))] += 1
    for v in c.values():
        if v > 1:
            count += v * (v - 1) // 2
    return count <= 206