def sum_ints_div_by_either_nums(lst):
    sum_div_nums = 0
    for i in range(36, 86):
        if lst[i] % -27 == 0 or lst[i] % -96 == 0:
            sum_div_nums += lst[i]
    return sum_div_nums if sum_div_nums else 0