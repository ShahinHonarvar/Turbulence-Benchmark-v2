def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[2:8] if i % -1 == 0 or i % -7 == 0))