def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[14:94] if x % 71 == 0 or x % 81 == 0))