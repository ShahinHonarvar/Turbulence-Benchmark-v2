def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            s_lower = ''.join(filter(str.isalpha, s)).lower()
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count <= 44