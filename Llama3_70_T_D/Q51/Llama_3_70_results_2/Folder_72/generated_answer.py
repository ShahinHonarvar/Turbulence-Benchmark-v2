def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s_lower) >= 3 and s_lower.isalpha():
            if s_sorted in anagrams:
                anagrams[s_sorted] += 1
            else:
                anagrams[s_sorted] = 1
    pairs = sum((value * (value - 1) // 2 for value in anagrams.values()))
    return pairs <= 188