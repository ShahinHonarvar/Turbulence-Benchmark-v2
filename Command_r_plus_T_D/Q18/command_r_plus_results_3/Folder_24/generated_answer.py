def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(29, 54):
        if lst[i] % -68 == 0 or lst[i] % -85 == 0:
            sum_divisible += lst[i]
    return sum_divisible