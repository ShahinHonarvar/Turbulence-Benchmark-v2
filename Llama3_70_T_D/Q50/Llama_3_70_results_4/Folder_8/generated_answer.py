def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.casefold())) for s in lst if len(s) >= 3]
    anagrams_count = len(lst) - len(set(lst))
    pairs_count = anagrams_count * (anagrams_count - 1) // 2
    return pairs_count >= 85