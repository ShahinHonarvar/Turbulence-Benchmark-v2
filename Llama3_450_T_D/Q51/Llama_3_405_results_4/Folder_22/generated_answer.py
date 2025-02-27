def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            s_lower = ''.join(sorted(s.lower()))
            if s_lower in anagrams:
                anagrams[s_lower] += 1
            else:
                anagrams[s_lower] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
        if count > 14:
            return False
    return True