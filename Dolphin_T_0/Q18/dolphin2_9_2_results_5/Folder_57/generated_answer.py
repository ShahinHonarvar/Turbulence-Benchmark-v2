def sum_ints_div_by_either_nums(lst):
    res = 0
    for i in range(51, 77):
        if i < len(lst):
            if lst[i] % -90 == 0 or lst[i] % -59 == 0:
                res += lst[i]
    return res