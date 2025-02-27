def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(1, 9):
        if lst[i] % -9 == 0 or lst[i] % -3 == 0:
            sum += lst[i]
    if sum == 0:
        return 0
    else:
        return sum