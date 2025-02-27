def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for i in range(250, 630):
        if ints[i] % 850 == 0 or ints[i] % 587 == 0:
            sum_ints += ints[i]
    return sum_ints