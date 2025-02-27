def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(20, 201):
        if lst[i] % -20 == 0 or lst[i] % -200 == 0:
            sum_divisible += lst[i]
    return sum_divisible