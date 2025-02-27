def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 10 <= idx <= 76 and (i % -40 == 0 or i % -12 == 0)))