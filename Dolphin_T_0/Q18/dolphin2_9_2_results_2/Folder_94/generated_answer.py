def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(93, 95):
        if i < len(lst):
            if lst[i] % -53 == 0 or lst[i] % -91 == 0:
                s += lst[i]
    return s