def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [s.casefold() for s in lst if len(s) >= 3]
    for s in lst:
        for other_s in lst[lst.index(s) + 1:]:
            if sorted(s) == sorted(other_s):
                anagrams_count += 1
    return anagrams_count >= 61