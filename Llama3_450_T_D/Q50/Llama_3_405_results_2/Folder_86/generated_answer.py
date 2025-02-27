def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s_lower)
            else:
                anagrams[sorted_s] = [s_lower]
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 115