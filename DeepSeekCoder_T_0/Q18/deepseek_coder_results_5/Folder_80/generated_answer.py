def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[14:94] if x % 71 == 0 or x % 81 == 0))