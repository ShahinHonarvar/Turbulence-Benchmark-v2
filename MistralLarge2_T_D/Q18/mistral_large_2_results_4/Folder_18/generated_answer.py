def sum_ints_div_by_either_nums(ints):
    return sum((x for i, x in enumerate(ints) if 55 <= i <= 66 and (x % 22 == 0 or x % 82 == 0)))