def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(3, 10):
        if lst[i] % 6 == 0 or lst[i] % 1 == 0:
            s += lst[i]
    return s