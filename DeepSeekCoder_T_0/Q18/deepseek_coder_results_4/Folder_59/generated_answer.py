def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[:9] if x % -3 == 0 or x % 8 == 0))