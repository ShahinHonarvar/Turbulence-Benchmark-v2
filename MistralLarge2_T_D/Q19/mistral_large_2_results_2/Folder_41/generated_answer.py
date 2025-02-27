def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[1:9]) if x % -3 != 0]