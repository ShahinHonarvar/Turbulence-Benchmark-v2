def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in (0, 1) and (x % 2 == 0 or x % 1 == 0)))