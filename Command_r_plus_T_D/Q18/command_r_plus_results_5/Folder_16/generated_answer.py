def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(55, 81):
        if lst[i] % 22 == 0 or lst[i] % 32 == 0:
            sum += lst[i]
    return sum