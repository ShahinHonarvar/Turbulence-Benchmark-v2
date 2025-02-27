def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i == 0 and x % 1 == 0))