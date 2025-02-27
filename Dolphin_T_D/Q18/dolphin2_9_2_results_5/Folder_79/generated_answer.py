def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(8, 10):
        if -3 in lst[i] or 6 in lst[i]:
            s += lst[i]
    return s