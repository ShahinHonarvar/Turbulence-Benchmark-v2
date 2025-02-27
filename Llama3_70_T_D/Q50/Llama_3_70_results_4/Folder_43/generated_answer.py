def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.casefold())) for s in strings if len(s) >= 3]
    anagrams = {}
    count = 0
    for s in strings:
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    for c in anagrams.values():
        count += c * (c - 1) // 2
    return count >= 61