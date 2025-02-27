def sum_ints_div_by_either_nums(lis):
    sum = 0
    for i in range(306, 958):
        if lis[i] % 982 == 0 or lis[i] % 319 == 0:
            sum += lis[i]
    return sum