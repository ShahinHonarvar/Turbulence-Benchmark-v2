def sum_ints_div_by_either_nums(lst):
    if len(lst) < 88:
        return 0
    total = 0
    for i in range(42, 88):
        if lst[i] % -90 == 0 or lst[i] % -74 == 0:
            total += lst[i]
    return total