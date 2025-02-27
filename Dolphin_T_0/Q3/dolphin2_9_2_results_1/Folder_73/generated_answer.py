def all_pos_ints_inclusive(lst):
    target_lst = [x for x in lst[19:93] if x > 0]
    if target_lst:
        return target_lst
    else:
        return []