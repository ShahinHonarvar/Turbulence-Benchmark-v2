def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[2:], 2) if i < 2 and x % 2 != 0]