def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            pairs += len(anagrams[sorted_s])
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for v in anagrams.values():
        pairs += len(v) * (len(v) - 1) // 2
    return pairs <= 59