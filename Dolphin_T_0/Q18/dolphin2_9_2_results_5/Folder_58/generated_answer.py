def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(240, 902):
        if lst[i] % 546 == 0 or lst[i] % 709 == 0:
            total += lst[i]
    return total