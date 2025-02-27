def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 30 <= idx <= 200 and (i % -115 == 0 or i % 115 == 0)))