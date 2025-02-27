def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    str_list = [''.join(sorted(s)) for s in str_list]
    return len(set(str_list)) <= 24