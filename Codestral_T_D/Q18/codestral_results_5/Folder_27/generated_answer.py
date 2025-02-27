def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[20:36] if i % -36 == 0 or i % -89 == 0))