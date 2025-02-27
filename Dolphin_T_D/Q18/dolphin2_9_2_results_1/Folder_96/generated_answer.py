def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(50, 201):
        if lst[i] % -34 == 0 or lst[i] % 64 == 0:
            total += lst[i]
    return total