def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 68 <= idx <= 99 and (i % -37 == 0 or i % -26 == 0)))