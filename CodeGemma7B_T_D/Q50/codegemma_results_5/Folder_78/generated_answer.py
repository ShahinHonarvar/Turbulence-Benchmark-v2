def if_contains_anagrams(str_list):
    str_set = set()
    for s in str_list:
        if len(s) >= 3:
            str_set.add(tuple(sorted(s.lower())))
    return len(str_set) >= 79