def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(81, 90):
        if i < len(lst):
            if lst[i] % 56 == 0 or lst[i] % 68 == 0:
                s += lst[i]
    return s