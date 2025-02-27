def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[:7] if i % -5 == 0 or i % -6 == 0))