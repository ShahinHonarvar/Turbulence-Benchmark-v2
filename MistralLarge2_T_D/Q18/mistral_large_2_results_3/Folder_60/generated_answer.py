def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[10:80] if x % -74 == 0 or x % -58 == 0))