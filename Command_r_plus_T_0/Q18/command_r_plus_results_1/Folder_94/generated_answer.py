def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(93, 95):
        if lst[i] % -53 == 0 or lst[i] % -91 == 0:
            sum_divisible += lst[i]
    return sum_divisible