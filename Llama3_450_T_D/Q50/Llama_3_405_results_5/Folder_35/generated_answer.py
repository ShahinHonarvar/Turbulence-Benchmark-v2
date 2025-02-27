def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s_lower)
            else:
                anagrams[sorted_str] = [s_lower]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 153