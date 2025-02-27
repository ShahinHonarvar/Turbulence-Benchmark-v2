def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 57 <= idx <= 84 and (i % -30 == 0 or i % -88 == 0)))