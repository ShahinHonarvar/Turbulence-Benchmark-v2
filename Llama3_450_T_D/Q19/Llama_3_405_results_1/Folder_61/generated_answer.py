def all_ints_not_div_by_num(lst):
    return [i for i in range(1, 6) if i not in [x for x in lst if x % -6 == 0]]