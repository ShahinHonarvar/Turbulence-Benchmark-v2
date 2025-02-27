def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(11, 77):
        if i in lst and (lst[i] % -81 == 0 or lst[i] % -94 == 0):
            s += lst[i]
    return s