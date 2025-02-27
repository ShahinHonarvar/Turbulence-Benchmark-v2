def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(57, 86):
        if lst[i] % -77 == 0 or lst[i] % -32 == 0:
            total += lst[i]
    return total