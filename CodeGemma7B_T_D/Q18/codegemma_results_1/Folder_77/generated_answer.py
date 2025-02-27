def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(828, 933):
        if lst[i] % 649 == 0 or lst[i] % 461 == 0:
            sum_divisible += lst[i]
    return sum_divisible if sum_divisible != 0 else 0