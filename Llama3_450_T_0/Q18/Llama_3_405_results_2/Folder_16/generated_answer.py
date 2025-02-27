def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[55:81] if i % 22 == 0 or i % 32 == 0))