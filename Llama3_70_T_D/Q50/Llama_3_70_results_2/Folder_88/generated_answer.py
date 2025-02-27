def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 34