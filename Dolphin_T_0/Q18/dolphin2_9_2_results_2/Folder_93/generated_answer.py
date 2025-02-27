def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(86, 90):
        if i in lst and (lst[i] % -61 == 0 or lst[i] % -79 == 0):
            total += lst[i]
    return total