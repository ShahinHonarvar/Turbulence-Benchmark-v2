def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(68, 100):
        if lst[i] % -37 == 0 or lst[i] % -26 == 0:
            total += lst[i]
    return total