def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(154, 799):
        if ints[i] % 275 == 0 or ints[i] % 580 == 0:
            total += ints[i]
    return total