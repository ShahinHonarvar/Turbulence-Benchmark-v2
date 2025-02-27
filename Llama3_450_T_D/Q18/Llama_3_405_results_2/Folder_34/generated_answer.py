def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 60 <= idx <= 200 and (i % 9 == 0 or i % 11 == 0)))