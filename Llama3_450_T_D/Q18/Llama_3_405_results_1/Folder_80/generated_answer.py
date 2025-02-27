def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 14 <= idx <= 93 and (i % 71 == 0 or i % 81 == 0)))