def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(11, 77):
        if lst[i] % -81 == 0 or lst[i] % -94 == 0:
            total += lst[i]
    return total