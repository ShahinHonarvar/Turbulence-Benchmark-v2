def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 34 <= idx <= 81 and (i % 27 == 0 or i % 57 == 0)))