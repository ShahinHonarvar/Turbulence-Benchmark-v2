def if_contains_anagrams(str_list):
    str_dict = {}
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s not in str_dict:
            str_dict[s] = True
    return len(str_dict) <= 49