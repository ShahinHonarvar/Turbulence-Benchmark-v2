def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(81, 90):
        if lst[i] % 56 == 0 or lst[i] % 68 == 0:
            sum_divisible += lst[i]
    return sum_divisible