def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(50, 201):
        if ints[i] % -34 == 0 or ints[i] % 64 == 0:
            total += ints[i]
    return total if total != 0 else 0