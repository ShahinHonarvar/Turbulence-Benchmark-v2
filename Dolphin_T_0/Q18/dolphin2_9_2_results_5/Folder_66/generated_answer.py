def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(58, 82):
        if lst[i] % 55 == 0 or lst[i] % 10 == 0:
            total += lst[i]
    return total