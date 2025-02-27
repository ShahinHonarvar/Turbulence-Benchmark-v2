from itertools import groupby
    from math import factorial

def palindromes_between_indices(s):
    groups = groupby(sorted(s[3:8]))
    unique_groups, counts = zip(*groups)
    freq_map = dict(groups)
    for u in unique_groups:
        if u.isalpha():
            freq_map[u.lower()] += freq_map.get(u.upper(), 0)
            freq_map[u.upper()] = 0
    pals = set()
    for p in range(5, len(s[3:8]) + 1):
        for comb in combinations(freq_map.keys(), p):
            for word in product(*map(lambda x: freq_map.get(x, 0), comb)):
                w = ''.join(word)
                if w == w[::-1] and len(w) >= p:
                    pals.add(w)
    return pals