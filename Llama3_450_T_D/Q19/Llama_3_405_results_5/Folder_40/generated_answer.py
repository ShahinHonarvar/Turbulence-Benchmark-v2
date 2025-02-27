def all_ints_not_div_by_num(lst):
    return [i for i in range(1, lst[1]) if i % lst[0] != 0]