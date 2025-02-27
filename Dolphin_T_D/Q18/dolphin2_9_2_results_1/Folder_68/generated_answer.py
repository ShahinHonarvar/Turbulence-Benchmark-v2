def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(7, 8):
        if lst[i] % 5 == 0 or lst[i] % 7 == 0:
            total += lst[i]
    return total