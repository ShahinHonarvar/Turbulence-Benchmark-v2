def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s] = anagrams.get(s, 0) + 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) >= 19