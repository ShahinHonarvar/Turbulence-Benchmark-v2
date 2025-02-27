from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for w in lst:
        if len(w) >= 3:
            c[tuple(sorted(w.lower()))] += 1
    return sum((n * (n - 1) // 2 for n in c.values() >= 79))