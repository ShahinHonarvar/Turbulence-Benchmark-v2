def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(78, 82):
        if i in lst:
            if lst[i] % 60 == 0 or lst[i] % 76 == 0:
                total += lst[i]
    return total