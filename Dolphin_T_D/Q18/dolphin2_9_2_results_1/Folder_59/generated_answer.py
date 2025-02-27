def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[:9] if val % -3 == 0 or val % 8 == 0))