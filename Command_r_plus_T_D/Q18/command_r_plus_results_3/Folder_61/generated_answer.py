def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(7):
        if lst[i] % -5 == 0 or lst[i] % -6 == 0:
            sum_divisible += lst[i]
    return sum_divisible