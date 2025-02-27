def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(24, 33):
        if lst[i] % 35 == 0 or lst[i] % 87 == 0:
            total += lst[i]
    return total