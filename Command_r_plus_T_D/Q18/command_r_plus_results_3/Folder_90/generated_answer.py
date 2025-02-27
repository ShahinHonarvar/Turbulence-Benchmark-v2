def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(138, 425):
        if lst[i] % -863 == 0 or lst[i] % -329 == 0:
            sum_divisible += lst[i]
    return sum_divisible