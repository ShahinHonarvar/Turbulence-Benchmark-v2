def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(sorted(set(s.casefold())))
        if len(s) >= 3 and s.isalpha():
            anagrams[s] = anagrams.get(s, 0) + 1
    count = 0
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 75