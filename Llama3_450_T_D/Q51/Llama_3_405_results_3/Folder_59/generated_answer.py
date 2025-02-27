def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 15