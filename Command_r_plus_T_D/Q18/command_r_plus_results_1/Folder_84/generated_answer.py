def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(78, 82):
        if lst[i] % 76 == 0 or lst[i] % 60 == 0:
            sum_divisible += lst[i]
    return sum_divisible