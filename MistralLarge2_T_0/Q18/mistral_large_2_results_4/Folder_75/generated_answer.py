def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 20 <= i <= 93 and (x % -92 == 0 or x % -50 == 0)))