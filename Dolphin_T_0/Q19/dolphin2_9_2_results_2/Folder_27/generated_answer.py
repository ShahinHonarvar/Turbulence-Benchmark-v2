def all_ints_not_div_by_num(lst):
    if 14 <= len(lst) < 21:
        return [x for x in lst[14:21] if x % -93 != 0]
    else:
        return []