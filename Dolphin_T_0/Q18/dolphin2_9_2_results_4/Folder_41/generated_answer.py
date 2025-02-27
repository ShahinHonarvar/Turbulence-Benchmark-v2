def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[0:10] if i % 6 == 0 or i % -3 == 0))