def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[50:93] if i % -94 == 0 or i % -95 == 0))