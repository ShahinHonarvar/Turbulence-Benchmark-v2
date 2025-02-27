def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams_count:
            anagrams_count[s_sorted] += 1
        else:
            anagrams_count[s_sorted] = 1
    pairs_count = 0
    for count in anagrams_count.values():
        pairs_count += count * (count - 1) // 2
    return pairs_count <= 22