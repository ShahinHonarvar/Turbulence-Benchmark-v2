def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(90, 98):
        if lst[i] % 13 == 0 or lst[i] % 35 == 0:
            sum_divisible += lst[i]
    return sum_divisible