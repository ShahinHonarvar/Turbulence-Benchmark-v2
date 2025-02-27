def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        anagrams_count[s_sorted] = anagrams_count.get(s_sorted, 0) + 1
    anagrams_pairs = sum((v * (v - 1) // 2 for v in anagrams_count.values()))
    return anagrams_pairs <= 36