def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 8 <= i <= 9 and (x % -3 == 0 or x % 6 == 0)))