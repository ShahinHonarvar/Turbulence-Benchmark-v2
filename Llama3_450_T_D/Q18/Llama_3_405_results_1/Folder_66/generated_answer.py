def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 58 <= idx <= 81 and (i % 55 == 0 or i % 10 == 0)))