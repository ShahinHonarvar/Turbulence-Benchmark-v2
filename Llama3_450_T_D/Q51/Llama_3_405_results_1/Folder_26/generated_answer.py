def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower.isalpha():
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 35