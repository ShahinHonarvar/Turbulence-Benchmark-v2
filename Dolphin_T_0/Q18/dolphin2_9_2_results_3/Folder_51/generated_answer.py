def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(6, 10):
        if lst[i] % -1 == 0 or lst[i] % -10 == 0:
            sum_nums += lst[i]
    return sum_nums if sum_nums != 0 else 0