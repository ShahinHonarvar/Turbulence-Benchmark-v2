def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(44, 60):
        if i in lst and (lst[i] % 39 == 0 or lst[i] % 15 == 0):
            total += lst[i]
    return total