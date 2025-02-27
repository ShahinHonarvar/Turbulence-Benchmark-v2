def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[1:8]) if x % 7 != 0]