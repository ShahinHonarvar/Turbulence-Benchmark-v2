def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(36, 86):
        if lst[i] % -27 == 0 or lst[i] % -96 == 0:
            total += lst[i]
    return total if total != 0 else None