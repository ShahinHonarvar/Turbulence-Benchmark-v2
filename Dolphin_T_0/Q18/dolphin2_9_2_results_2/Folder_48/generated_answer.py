def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(306, 958):
        if ints[i] % 982 == 0 or ints[i] % 319 == 0:
            total += ints[i]
    return total if total else 0