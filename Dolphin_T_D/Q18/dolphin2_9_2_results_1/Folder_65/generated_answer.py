def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(len(lst)):
        if i >= 50 and i <= 92:
            if lst[i] % -94 == 0 or lst[i] % -95 == 0:
                total += lst[i]
    return total