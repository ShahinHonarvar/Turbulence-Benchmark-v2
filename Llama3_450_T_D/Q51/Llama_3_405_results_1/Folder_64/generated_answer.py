def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s.isalpha():
            anagrams[s] = anagrams.get(s, 0) + 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 59