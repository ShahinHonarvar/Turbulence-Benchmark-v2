def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(9):
        if lst[i] % -3 == 0 or lst[i] % 8 == 0:
            total_sum += lst[i]
    return total_sum