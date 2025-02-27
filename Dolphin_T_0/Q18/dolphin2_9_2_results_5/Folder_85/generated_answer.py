def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(1, 9):
        if ints[i] % -9 == 0 or ints[i] % -3 == 0:
            sum_ints += ints[i]
    return sum_ints