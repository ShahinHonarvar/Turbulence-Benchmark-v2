def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 70 <= i <= 200 and (x % 3 == 0 or x % -300 == 0)))