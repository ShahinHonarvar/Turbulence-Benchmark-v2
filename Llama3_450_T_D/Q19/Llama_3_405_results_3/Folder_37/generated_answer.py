def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 1 < i < len(lst) - 1 and x % 5 != 0]