def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(29, 54):
        if lst[i] % -68 == 0 or lst[i] % -85 == 0:
            total += lst[i]
    return total or 0