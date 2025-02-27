def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 24