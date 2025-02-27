def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(828, 933):
        if lst[i] % -649 == 0 or lst[i] % -461 == 0:
            sum_nums += lst[i]
    return sum_nums