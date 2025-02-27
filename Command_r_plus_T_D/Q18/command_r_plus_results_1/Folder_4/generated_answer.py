def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(86, 91):
        if lst[i] % -71 == 0 or lst[i] % -67 == 0:
            sum_divisible += lst[i]
    return sum_divisible