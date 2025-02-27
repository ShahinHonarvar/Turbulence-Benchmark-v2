def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(4):
        if lst[i] % 11 == 0 or lst[i] % -7 == 0:
            total_sum += lst[i]
    return total_sum