def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    count = 0
    for a in anagrams:
        count += anagrams[a] * (anagrams[a] - 1) // 2
    return count >= 55