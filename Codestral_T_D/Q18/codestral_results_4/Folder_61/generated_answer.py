def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[0:7] if x % -5 == 0 or x % -6 == 0))