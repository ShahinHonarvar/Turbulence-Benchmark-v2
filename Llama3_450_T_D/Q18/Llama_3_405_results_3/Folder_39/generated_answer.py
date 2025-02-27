def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 13 <= idx <= 76 and (i % -66 == 0 or i % -32 == 0)))