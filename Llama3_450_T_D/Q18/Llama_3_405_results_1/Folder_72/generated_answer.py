def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 38 <= idx <= 81 and (i % -61 == 0 or i % -71 == 0)))