def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[1:5] if i % 4 == 0 or i % -6 == 0))