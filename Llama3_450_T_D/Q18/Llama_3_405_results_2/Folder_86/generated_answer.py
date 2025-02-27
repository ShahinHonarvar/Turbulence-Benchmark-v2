def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 54 <= idx <= 79 and (i % 54 == 0 or i % 28 == 0)))