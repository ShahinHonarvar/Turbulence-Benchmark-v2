def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s_lower)
            else:
                anagrams[sorted_str] = [s_lower]
    count = 0
    for value in anagrams.values():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 14