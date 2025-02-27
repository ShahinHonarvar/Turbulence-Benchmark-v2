def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 10 <= i <= 100 and (x % 10 == 0 or x % 100 == 0)))