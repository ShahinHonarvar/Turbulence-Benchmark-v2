def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(48, 60, 1):
        if lst[i] % 88 == 0 or lst[i] % 58 == 0:
            sum += lst[i]
    if sum == 0:
        return 0
    else:
        return sum