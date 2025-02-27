def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[:9]) if i < 8 and x % -3 != 0]