def all_ints_not_div_by_num(lst):
    return [x for x in lst if 1 < lst.index(x) < 2 and x % 8 != 0]