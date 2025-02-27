from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            d[''.join(sorted(s.lower()))].append(s)
    return any((len(v) >= 2 for v in d.values()))