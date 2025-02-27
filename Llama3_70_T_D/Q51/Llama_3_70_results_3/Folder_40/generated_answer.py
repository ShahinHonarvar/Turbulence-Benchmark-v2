def if_contains_anagrams(lst):
    anagram_set = set()
    pairs_count = 0
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_set:
            pairs_count += 1
        anagram_set.add(sorted_s)
    return pairs_count <= 29