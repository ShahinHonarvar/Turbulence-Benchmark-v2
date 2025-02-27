def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 86 <= i <= 89 and (x % -61 == 0 or x % -79 == 0)))