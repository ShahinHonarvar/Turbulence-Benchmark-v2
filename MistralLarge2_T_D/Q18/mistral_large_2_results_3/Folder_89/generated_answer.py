def sum_ints_div_by_either_nums(ints):
    return sum((x for i, x in enumerate(ints) if 28 <= i <= 96 and (x % 90 == 0 or x % 97 == 0)))