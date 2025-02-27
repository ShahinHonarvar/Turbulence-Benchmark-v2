def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 86 <= idx <= 90 and (i % -71 == 0 or i % -67 == 0)))