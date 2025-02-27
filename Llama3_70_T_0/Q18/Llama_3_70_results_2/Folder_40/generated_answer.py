def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[:2] if i % 2 == 0 or i % 1 == 0))