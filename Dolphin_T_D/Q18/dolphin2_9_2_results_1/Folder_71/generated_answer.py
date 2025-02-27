def sum_ints_div_by_either_nums(lst):
    sum_ints = 0
    for i in range(68, 100):
        if lst[i] % -37 == 0 or lst[i] % -26 == 0:
            sum_ints += lst[i]
    return sum_ints if sum_ints != 0 else 0