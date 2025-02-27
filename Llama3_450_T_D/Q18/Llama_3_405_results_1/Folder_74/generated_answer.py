def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 90 <= idx <= 97 and (i % 13 == 0 or i % 35 == 0)))