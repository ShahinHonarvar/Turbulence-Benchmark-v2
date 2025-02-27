def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i == 0 and x % 7 == 0]