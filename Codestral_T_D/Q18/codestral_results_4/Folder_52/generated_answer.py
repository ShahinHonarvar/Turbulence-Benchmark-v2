def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(48, 60):
        if lst[i] % 88 == 0 or lst[i] % 58 == 0:
            total += lst[i]
    return total