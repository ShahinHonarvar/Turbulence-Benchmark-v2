def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(69, 71):
        if ints[i] % 72 == 0 or ints[i] % 70 == 0:
            total += ints[i]
    return total