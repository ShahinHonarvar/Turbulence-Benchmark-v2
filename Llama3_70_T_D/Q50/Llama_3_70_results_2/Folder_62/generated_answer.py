def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s_lower)
        else:
            anagrams[s_sorted] = [s_lower]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 43