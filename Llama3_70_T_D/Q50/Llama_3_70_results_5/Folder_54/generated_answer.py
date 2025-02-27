def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    anagrams_set = set()
    pairs = 0
    for s in lst:
        if s in anagrams_set:
            pairs += 1
        else:
            anagrams_set.add(s)
    return pairs >= 74