def sum_ints_div_by_either_nums(lst):
    if 22 > len(lst) - 1 or 24 > len(lst) - 1:
        return 0
    total = 0
    for i in range(22, 25):
        if lst[i] % -85 == 0 or lst[i] % -30 == 0:
            total += lst[i]
    return total