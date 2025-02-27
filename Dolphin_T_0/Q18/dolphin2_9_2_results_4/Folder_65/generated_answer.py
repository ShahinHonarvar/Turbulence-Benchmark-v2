def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[50:93] if val % -94 == 0 or val % -95 == 0))