def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[20:94] if val % -92 == 0 or val % -50 == 0))