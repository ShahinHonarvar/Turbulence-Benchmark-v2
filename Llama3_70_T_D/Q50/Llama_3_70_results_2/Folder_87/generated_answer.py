def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 88