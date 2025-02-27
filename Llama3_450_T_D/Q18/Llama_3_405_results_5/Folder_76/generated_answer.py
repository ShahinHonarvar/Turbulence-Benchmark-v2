def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 250 <= idx <= 629 and (i % 850 == 0 or i % 587 == 0)))