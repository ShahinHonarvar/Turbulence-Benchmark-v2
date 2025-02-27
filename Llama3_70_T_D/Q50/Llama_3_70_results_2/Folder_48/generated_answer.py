def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagrams:
                count += anagrams[sorted_str]
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    return count >= 219