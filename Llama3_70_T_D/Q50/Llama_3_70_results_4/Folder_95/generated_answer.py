def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    count = len(lst) - len(set(lst))
    return count >= 93