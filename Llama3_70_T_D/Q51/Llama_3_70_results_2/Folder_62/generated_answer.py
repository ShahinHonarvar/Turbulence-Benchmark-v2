def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        s = ''.join(sorted((c for c in string.lower() if c.isalpha())))
        if len(s) >= 3:
            anagrams[s] = anagrams.get(s, 0) + 1
    return sum((n * (n - 1) // 2 for n in anagrams.values())) <= 289