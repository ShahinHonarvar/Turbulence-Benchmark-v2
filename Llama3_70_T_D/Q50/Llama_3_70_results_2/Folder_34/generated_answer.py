def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            s_sorted = ''.join(sorted(s_lower))
            if s_sorted in anagrams:
                anagrams[s_sorted] += 1
            else:
                anagrams[s_sorted] = 1
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs >= 25