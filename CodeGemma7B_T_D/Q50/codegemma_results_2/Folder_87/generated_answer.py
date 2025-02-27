def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    str_dict = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in str_dict:
            str_dict[sorted_s] = [s]
        else:
            str_dict[sorted_s].append(s)
    if len([v for v in str_dict.values() if len(v) >= 88]) >= 1:
        return True
    return False