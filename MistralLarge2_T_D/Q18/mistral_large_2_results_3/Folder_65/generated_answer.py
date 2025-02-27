def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[50:93] if i % -94 == 0 or i % -95 == 0))