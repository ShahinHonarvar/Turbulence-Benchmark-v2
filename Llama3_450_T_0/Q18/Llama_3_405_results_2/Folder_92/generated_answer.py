def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[0:1] if i % 1 == 0 or i % -1 == 0))