def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(20, 201):
        if lst[i] % -20 == 0 or lst[i] % -200 == 0:
            total += lst[i]
    return total