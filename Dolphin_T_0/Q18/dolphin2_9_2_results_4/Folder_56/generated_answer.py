def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(7, 10):
        if lst[i] % -9 == 0 or lst[i] % -7 == 0:
            s += lst[i]
    return s