def sum_ints_div_by_either_nums(lst):
    sum_ints = 0
    for i in range(10, 77):
        if lst[i] % -40 == 0 or lst[i] % -12 == 0:
            sum_ints += lst[i]
    return sum_ints