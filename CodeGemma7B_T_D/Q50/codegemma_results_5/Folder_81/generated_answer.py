def if_contains_anagrams(str_list):
    str_set = set()
    for str in str_list:
        str_set.add(tuple(sorted(str.lower())))
    return len(str_set) >= 16