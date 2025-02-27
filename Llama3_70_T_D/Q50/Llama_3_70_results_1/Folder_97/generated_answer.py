def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s_lower)
        else:
            anagrams[sorted_str] = [s_lower]
    count = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values()))
    return count >= 123