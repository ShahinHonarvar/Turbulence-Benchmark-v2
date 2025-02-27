def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if s_lower in anagrams:
                anagrams[s_lower] += 1
            else:
                anagrams[s_lower] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count >= 85