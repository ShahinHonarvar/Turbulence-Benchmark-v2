def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    pairs = 0
    for v in anagrams.values():
        n = len(v)
        pairs += n * (n - 1) // 2
    return pairs <= 60