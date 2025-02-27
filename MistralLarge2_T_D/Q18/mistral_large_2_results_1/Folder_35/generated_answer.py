def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[77:88] if x % 23 == 0 or x % 57 == 0))