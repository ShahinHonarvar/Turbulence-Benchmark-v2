def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(81, 87):
        if lst[i] % -33 == 0 or lst[i] % -62 == 0:
            sum_divisible += lst[i]
    return sum_divisible