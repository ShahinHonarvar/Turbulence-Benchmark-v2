def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(48, 77):
        if lst[i] % -46 == 0 or lst[i] % -82 == 0:
            sum += lst[i]
    return sum