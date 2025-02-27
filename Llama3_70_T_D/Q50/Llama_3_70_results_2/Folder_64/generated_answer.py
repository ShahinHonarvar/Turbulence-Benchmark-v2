def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s_lower) >= 3:
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s_lower)
            else:
                anagrams[s_sorted] = [s_lower]
    pairs = 0
    for a in anagrams:
        pairs += len(anagrams[a]) * (len(anagrams[a]) - 1) // 2
    return pairs >= 5