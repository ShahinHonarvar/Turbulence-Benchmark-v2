def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(80, 201):
        if lst[i] % 10 == 0 or lst[i] % 1000 == 0:
            total_sum += lst[i]
    return total_sum