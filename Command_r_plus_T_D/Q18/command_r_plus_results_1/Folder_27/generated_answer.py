def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(20, 36):
        if lst[i] % -36 == 0 or lst[i] % -89 == 0:
            sum_divisible += lst[i]
    return sum_divisible