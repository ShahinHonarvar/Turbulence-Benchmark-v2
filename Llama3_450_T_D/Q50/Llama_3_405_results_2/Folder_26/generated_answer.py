def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    pairs = 0
    for a in anagrams.values():
        n = len(a)
        pairs += n * (n - 1) // 2
    return pairs >= 49