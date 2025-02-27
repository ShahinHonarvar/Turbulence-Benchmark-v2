def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(90, 98):
        total += lst[i] * (lst[i] % 13 == 0 or lst[i] % 35 == 0)
    return total