def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(80, 201):
        if ints[i] % 10 == 0 or ints[i] % 1000 == 0:
            total += ints[i]
    return total