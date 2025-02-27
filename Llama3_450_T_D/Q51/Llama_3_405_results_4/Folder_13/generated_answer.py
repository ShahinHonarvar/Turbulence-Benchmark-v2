def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3 and s.isalpha()]
    anagrams = {}
    for s in strings:
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 54