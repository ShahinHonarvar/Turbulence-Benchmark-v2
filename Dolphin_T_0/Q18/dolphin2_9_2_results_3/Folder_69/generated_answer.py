def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[61:89] if val % 31 == 0 or val % 11 == 0))