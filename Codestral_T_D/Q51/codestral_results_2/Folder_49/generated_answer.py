def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) < 3:
            continue
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count <= 10