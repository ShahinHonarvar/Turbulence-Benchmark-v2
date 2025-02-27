def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s_lower) >= 3:
            if s_sorted in anagrams:
                anagrams[s_sorted] += 1
            else:
                anagrams[s_sorted] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 50