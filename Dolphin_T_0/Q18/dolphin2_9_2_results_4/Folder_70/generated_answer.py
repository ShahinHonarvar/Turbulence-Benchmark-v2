def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(42, 44):
        if ints[i] % 15 == 0 or ints[i] % 87 == 0:
            sum += ints[i]
    return sum