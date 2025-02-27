def all_ints_not_div_by_num(lst):
    return [i for i in range(lst[0] + 1, lst[1]) if i % -1 != 0]