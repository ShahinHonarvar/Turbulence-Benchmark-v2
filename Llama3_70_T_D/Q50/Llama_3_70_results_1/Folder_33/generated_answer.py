def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s_lower)
        else:
            anagrams[s_sorted] = [s_lower]
    for v in anagrams.values():
        if len(v) > 1 and len(v[0]) >= 3:
            count += len(v) * (len(v) - 1) // 2
    return count >= 140