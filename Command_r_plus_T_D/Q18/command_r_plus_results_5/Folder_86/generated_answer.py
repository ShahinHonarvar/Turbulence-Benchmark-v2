def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(54, 80):
        if lst[i] % 54 == 0 or lst[i] % 28 == 0:
            total_sum += lst[i]
    return total_sum