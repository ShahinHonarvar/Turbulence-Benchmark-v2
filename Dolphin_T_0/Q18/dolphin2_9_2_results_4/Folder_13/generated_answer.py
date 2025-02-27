def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(13, 19):
        if ints[i] % 45 == 0 or ints[i] % 20 == 0:
            sum += ints[i]
    return sum