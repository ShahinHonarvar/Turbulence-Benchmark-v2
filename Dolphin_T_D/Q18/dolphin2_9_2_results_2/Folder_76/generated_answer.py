def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(250, 630):
        if ints[i] % 850 == 0 or ints[i] % 587 == 0:
            total += ints[i]
    return total if total else 0