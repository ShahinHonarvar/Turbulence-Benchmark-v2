def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            anagrams[sorted_str] = anagrams.get(sorted_str, 0) + 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs >= 123