def sum_ints_div_by_either_nums(lst):
    if 81 > len(lst) - 1 or 86 > len(lst) - 1:
        return 0
    sum_divisible = 0
    for i in range(81, 87):
        if lst[i] % -33 == 0 or lst[i] % -62 == 0:
            sum_divisible += lst[i]
    return sum_divisible