def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(41, 57):
        if lst[i] % 82 == 0 or lst[i] % 90 == 0:
            total += lst[i]
    return total