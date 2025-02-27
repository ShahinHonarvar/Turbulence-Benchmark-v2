def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[2:8] if i % -1 == 0 or i % -7 == 0))