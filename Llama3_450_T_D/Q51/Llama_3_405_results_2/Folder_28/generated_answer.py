def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        anagrams[s_sorted] = anagrams.get(s_sorted, 0) + 1
    count = 0
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 78