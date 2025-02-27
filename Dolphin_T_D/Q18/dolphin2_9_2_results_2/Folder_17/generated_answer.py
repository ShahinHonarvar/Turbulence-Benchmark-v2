def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(81, 90):
        if lst[i] % 56 == 0 or lst[i] % 68 == 0:
            total += lst[i]
    return total