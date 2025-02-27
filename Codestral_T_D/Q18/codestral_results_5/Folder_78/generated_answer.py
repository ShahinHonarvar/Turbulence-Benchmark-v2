def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[34:70] if val % 19 == 0 or val % 32 == 0))