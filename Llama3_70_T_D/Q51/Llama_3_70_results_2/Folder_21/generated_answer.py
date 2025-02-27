def if_contains_anagrams(lst):
    d = {}
    for s in lst:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    pairs = sum([v - 1 for v in d.values() if v > 1])
    return pairs <= 26