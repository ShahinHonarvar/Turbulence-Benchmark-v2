def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 41 <= idx <= 56 and (i % 82 == 0 or i % 90 == 0)))