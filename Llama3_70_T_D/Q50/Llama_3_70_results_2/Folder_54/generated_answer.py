def if_contains_anagrams(lst):
    lst = [''.join(sorted(s)).lower() for s in lst if len(s) >= 3]
    return len([lst.count(s) for s in set(lst) if lst.count(s) > 1]) >= 74