def sum_ints_div_by_either_nums(ints):
    return sum((x for i, x in enumerate(ints) if 57 <= i <= 84 and (x % -30 == 0 or x % -88 == 0)))