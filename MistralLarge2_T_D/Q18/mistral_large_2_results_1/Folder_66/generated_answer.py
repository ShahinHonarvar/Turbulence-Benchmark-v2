def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[58:82] if x % 55 == 0 or x % 10 == 0))