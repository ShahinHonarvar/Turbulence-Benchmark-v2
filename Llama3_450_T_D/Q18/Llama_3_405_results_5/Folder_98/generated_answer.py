def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[:6] if i % -1 == 0 or i % 13 == 0))