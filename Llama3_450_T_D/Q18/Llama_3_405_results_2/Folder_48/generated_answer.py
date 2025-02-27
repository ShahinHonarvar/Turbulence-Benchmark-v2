def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 306 <= idx <= 957 and (i % 982 == 0 or i % 319 == 0)))