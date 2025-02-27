def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(11, 77):
        if lst[i] % -81 == 0 or lst[i] % -94 == 0:
            sum += lst[i]
    return sum