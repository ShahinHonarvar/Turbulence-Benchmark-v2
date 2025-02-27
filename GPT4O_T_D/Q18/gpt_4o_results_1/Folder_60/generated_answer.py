def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[10:80] if x % 74 == 0 or x % 58 == 0))