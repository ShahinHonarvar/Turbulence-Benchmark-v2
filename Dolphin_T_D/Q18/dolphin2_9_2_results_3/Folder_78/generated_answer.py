def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(34, 70):
        if ints[i] % 19 == 0 or ints[i] % 32 == 0:
            sum += ints[i]
    return sum