def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, 0) + 1
    pair_count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pair_count <= 89