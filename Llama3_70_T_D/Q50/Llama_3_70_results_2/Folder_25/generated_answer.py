def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) < 3:
            continue
        s_lower = ''.join(sorted(s.lower()))
        if s_lower in anagrams:
            anagrams[s_lower] += 1
        else:
            anagrams[s_lower] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 14