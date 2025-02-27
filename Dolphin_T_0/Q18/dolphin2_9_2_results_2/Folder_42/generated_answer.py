def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(29, 46):
        if i in lst:
            if lst[i] % 27 == 0 or lst[i] % 81 == 0:
                total_sum += lst[i]
    return total_sum