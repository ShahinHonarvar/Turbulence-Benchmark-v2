def if_contains_anagrams(str_list):
    str_dict = {}
    for str_ in str_list:
        if not str_ or len(str_) < 3:
            continue
        str_ = str_.lower()
        str_sorted = ''.join(sorted(str_))
        if str_sorted in str_dict:
            str_dict[str_sorted] += 1
            if str_dict[str_sorted] >= 233:
                return True
        else:
            str_dict[str_sorted] = 1
    return False