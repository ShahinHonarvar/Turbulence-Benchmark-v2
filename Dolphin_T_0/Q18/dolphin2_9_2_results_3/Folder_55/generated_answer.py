def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(0, 10):
        if lst[i] % 10 == 0 or lst[i] % 100 == 0:
            sum_nums += lst[i]
    return sum_nums