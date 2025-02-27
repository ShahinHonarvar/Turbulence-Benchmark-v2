def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(46, 92):
        if lst[i] % 67 == 0 or lst[i] % 15 == 0:
            s += lst[i]
    return s if s != 0 else 0