def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(20, 36):
        if lst[i] % -36 == 0 or lst[i] % -89 == 0:
            total += lst[i]
    return total