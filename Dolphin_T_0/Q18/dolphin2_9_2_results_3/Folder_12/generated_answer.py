def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(35, 65):
        if i < len(lst) and (lst[i] % -30 == 0 or lst[i] % -95 == 0):
            total += lst[i]
    return total