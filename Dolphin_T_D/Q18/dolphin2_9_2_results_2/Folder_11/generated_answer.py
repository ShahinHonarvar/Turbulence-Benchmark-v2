def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(22, 25):
        if i >= len(lst):
            return 0
        if lst[i] % -85 == 0 or lst[i] % -30 == 0:
            total += lst[i]
    return total