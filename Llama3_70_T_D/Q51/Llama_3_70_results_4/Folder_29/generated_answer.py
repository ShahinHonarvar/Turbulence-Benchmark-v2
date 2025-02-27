def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            count += anagrams[s_sorted]
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    return count <= 318