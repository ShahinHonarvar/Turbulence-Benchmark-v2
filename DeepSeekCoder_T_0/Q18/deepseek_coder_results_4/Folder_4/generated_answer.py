def sum_ints_div_by_either_nums(lst):
    if 86 > len(lst) - 1 or 90 > len(lst) - 1:
        return 0
    total = 0
    for i in range(86, 91):
        if lst[i] % -71 == 0 or lst[i] % -67 == 0:
            total += lst[i]
    return total