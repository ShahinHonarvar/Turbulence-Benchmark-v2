def all_pos_ints_inclusive(lst):
    sub_lst = lst[32:37] if 32 < len(lst) else []
    return [i for i in sub_lst if i > 0]