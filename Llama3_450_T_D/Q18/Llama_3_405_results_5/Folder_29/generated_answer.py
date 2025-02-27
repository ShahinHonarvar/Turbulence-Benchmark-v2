def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 55 <= idx <= 84 and (i % -24 == 0 or i % -11 == 0)))