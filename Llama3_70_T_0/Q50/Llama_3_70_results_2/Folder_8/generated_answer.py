def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s_lower)
        else:
            anagrams[sorted_s] = [s_lower]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 85