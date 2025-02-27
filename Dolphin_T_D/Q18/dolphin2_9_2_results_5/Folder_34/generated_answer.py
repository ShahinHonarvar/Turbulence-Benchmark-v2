def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[60:201] if val % 9 == 0 or val % 11 == 0))