def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    pairs = 0
    for v in anagrams.values():
        if len(v) > 1:
            pairs += len(v) * (len(v) - 1) // 2
    return pairs >= 95