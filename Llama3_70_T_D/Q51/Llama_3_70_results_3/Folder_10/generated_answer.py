def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        if s_sorted in anagrams_count:
            anagrams_count[s_sorted] += 1
        else:
            anagrams_count[s_sorted] = 1
    pairs_count = sum((x * (x - 1) // 2 for x in anagrams_count.values()))
    return pairs_count <= 21