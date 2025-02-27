def sum_ints_div_by_either_nums(ints):
    return sum((ints[i] for i in range(7, 10) if ints[i] % -9 == 0 or ints[i] % -7 == 0))