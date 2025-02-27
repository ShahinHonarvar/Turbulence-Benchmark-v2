def sum_ints_div_by_either_nums(lst):
    sum_divisible_by_either = 0
    for i in range(25, 81):
        if lst[i] % -20 == 0 or lst[i] % -26 == 0:
            sum_divisible_by_either += lst[i]
    return sum_divisible_by_either