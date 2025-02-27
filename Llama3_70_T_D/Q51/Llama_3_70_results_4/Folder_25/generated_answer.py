def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s_sorted) >= 3 and s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 67