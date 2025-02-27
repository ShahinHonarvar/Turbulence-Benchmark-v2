def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[20:51]) if i % -48 != 0]