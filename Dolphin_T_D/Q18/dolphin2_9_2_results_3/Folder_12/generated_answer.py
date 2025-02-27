def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(35, 65):
        if lst[i] % -30 == 0 or lst[i] % -95 == 0:
            sum += lst[i]
    return sum