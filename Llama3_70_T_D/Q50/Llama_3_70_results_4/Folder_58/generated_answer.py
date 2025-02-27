def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagrams = {}
    count = 0
    for s in strings:
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count >= 411