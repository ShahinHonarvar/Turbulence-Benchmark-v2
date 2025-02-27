from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        s = ''.join(sorted([ch.lower() for ch in s if ch.isalpha()]))
        if len(s) >= 3:
            c[s] += 1
    pairs = sum((ci * (ci - 1) // 2 for ci in c.values() if ci > 1))
    return pairs <= 66