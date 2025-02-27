def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[0:4] if x % 11 == 0 or x % -7 == 0))