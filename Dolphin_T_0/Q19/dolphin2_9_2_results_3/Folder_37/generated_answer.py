def all_ints_not_div_by_num(lst):
    return [i for i in lst if 1 <= lst.index(i) < 2 and i % 5 != 0]