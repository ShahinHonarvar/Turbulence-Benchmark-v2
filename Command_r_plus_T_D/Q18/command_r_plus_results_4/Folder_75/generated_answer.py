def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(20, 94):
        if lst[i] % -92 == 0 or lst[i] % -50 == 0:
            sum_divisible += lst[i]
    return sum_divisible