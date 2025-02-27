def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 42 <= idx <= 87 and (i % -90 == 0 or i % -74 == 0)))