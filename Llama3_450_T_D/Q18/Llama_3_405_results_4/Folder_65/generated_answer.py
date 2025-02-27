def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 50 <= idx <= 92 and (i % -94 == 0 or i % -95 == 0)))