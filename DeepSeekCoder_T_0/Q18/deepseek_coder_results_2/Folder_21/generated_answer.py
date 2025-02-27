def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(315, 935):
        if i < len(lst) and (lst[i] % -897 == 0 or lst[i] % -556 == 0):
            total += lst[i]
    return total