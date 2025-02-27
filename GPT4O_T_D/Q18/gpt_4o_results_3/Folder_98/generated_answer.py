def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[:6] if x % 13 == 0 or x % -1 == 0))