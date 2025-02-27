def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 34 <= idx <= 69 and (i % 19 == 0 or i % 32 == 0)))