def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(70, 201):
        if lst[i] % 3 == 0 or lst[i] % -300 == 0:
            s += lst[i]
    return s