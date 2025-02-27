def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(73, 87):
        if i in lst and (lst[i] % 54 == 0 or lst[i] % 82 == 0):
            s += lst[i]
    return s if s != 0 else None