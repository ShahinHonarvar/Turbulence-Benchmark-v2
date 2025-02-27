def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(44, 60):
        if lst[i] % 39 == 0 or lst[i] % 15 == 0:
            sum_divisible += lst[i]
    return sum_divisible