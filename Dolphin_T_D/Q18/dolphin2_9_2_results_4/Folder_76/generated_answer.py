def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(250, 630):
        if ints[i] % 850 == 0 or ints[i] % 587 == 0:
            sum += ints[i]
    if sum == 0:
        return 0
    else:
        return sum