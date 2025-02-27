from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            d[''.join(sorted(s.lower()))].append(s)
    return sum((len(l) * (len(l) - 1) // 2 for l in d.values())) >= 43