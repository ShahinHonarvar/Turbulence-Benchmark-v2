def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for idx in range(1, 9):
        if lst[idx] % -9 == 0 or lst[idx] % -3 == 0:
            total_sum += lst[idx]
    return total_sum