def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(60, 201):
        if lst[i] % 9 == 0 or lst[i] % 11 == 0:
            sum_divisible += lst[i]
    return sum_divisible