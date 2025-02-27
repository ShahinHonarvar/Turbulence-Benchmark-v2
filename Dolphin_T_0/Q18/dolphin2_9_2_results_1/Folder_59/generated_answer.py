def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(9):
        if lst[i] % -3 == 0 or lst[i] % 8 == 0:
            s += lst[i]
    return s