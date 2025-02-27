from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for s in map(str.lower, lst):
        if len(s) < 3:
            continue
        c.update(Counter(s))
    return any((v >= 2 for v in c.values()))