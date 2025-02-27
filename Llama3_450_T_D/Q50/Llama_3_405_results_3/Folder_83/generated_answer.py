def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s_lower)
            else:
                anagrams[sorted_str] = [s_lower]
    for k in anagrams.values():
        count += len(k) * (len(k) - 1) // 2
    return count >= 48