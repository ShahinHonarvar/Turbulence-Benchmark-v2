def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 10 <= idx <= 79 and (i % -74 == 0 or i % -58 == 0)))