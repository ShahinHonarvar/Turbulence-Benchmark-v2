def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(20, 201):
        if ints[i] % -20 == 0 or ints[i] % -200 == 0:
            total += ints[i]
    return total