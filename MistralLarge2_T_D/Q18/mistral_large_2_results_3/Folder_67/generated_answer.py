def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[24:33] if i % 35 == 0 or i % 87 == 0))