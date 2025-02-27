def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(34, 70):
        if i < len(lst):
            if lst[i] % 19 == 0 or lst[i] % 32 == 0:
                total += lst[i]
    return total