def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(299, 383):
        if lst[i] % 858 == 0 or lst[i] % 952 == 0:
            sum_divisible += lst[i]
    return sum_divisible