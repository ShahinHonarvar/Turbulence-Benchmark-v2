def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 154 <= idx <= 798 and (i % 275 == 0 or i % 580 == 0)))