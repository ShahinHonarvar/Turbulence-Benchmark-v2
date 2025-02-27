def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 25 <= i <= 80 and (x % -20 == 0 or x % -26 == 0)))