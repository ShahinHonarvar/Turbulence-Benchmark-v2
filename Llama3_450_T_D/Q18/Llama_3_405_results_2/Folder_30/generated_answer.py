def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 11 <= idx <= 76 and (i % -81 == 0 or i % -94 == 0)))