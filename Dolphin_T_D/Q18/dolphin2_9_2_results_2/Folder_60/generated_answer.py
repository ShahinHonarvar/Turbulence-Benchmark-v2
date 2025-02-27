def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(10, 80):
        if lst[i] % -74 == 0 or lst[i] % -58 == 0:
            s += lst[i]
    return s