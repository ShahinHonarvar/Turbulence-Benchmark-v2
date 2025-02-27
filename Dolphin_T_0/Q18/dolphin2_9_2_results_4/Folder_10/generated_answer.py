def sum_ints_div_by_either_nums(lst):
    return sum((val for i, val in enumerate(lst[:100][32:], 32) if val % -11 == 0 or val % -15 == 0))