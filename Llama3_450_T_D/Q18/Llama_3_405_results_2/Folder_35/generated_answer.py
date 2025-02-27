def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 77 <= idx <= 87 and (i % 23 == 0 or i % 57 == 0)))