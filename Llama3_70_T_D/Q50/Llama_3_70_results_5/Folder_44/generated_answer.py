def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for v in anagrams.values():
        pairs += v * (v - 1) // 2
    return pairs >= 44