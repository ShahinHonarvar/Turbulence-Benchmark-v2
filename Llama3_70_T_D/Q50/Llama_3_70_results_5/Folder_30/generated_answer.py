def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count >= 78