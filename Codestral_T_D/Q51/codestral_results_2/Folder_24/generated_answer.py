def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    pair_count = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pair_count <= 96