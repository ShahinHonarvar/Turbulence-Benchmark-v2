def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted((c for c in s_lower if c.isalpha())))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 279