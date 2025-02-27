def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(25, 71):
        if lst[i] % 74 == 0 or lst[i] % 15 == 0:
            total += lst[i]
    return total