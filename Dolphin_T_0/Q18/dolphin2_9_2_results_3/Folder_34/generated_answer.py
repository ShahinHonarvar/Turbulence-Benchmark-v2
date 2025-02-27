def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(60, 201):
        if lst[i] % 9 == 0 or lst[i] % 11 == 0:
            total += lst[i]
    return total