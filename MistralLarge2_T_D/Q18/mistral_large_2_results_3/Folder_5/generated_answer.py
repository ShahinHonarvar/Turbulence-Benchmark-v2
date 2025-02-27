def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[:2] if x % -6 == 0 or x % 4 == 0))