def if_contains_anagrams(lst):
    sorted_lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    return len(sorted_lst) - len(set(sorted_lst)) <= 173