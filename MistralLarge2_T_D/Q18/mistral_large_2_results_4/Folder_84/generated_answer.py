def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 78 <= i <= 81 and (x % 76 == 0 or x % 60 == 0)))