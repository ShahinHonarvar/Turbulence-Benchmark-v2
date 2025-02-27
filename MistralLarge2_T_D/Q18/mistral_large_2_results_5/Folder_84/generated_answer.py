def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[78:82] if x % 76 == 0 or x % 60 == 0))