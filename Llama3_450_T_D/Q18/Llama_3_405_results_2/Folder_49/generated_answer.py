def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 80 <= idx <= 200 and (i % 10 == 0 or i % 1000 == 0)))