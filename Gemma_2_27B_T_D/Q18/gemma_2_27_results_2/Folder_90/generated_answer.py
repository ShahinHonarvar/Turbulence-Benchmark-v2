def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in range(138, 425):
        if ints[i] % -863 == 0 or ints[i] % -329 == 0:
            total += ints[i]
    return total