def sum_ints_div_by_either_nums(lst):
    if len(lst) < 10:
        return 0
    total = 0
    for i in range(7, 10):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0:
            total += lst[i]
    return total