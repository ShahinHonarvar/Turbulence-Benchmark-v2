def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(31, 51):
        if lst[i] % 81 == 0 or lst[i] % 64 == 0:
            sum_divisible += lst[i]
    return sum_divisible