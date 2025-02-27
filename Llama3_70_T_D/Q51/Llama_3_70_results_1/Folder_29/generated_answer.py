def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 318