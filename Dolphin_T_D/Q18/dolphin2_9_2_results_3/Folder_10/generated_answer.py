def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[32:100] if val % -11 == 0 or val % -15 == 0))