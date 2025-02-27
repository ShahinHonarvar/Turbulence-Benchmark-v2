def if_contains_anagrams(str_list):
    str_dict = {}
    str_list = [x.lower() for x in str_list]
    for st in str_list:
        if len(st) < 3:
            continue
        sorted_st = ''.join(sorted(st))
        if sorted_st not in str_dict:
            str_dict[sorted_st] = [st]
        else:
            str_dict[sorted_st].append(st)
    if len(str_dict) > 4:
        return False
    return True