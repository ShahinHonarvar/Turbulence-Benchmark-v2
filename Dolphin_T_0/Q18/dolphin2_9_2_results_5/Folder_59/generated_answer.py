def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(9):
        if lst[i] % -3 == 0 or lst[i] % 8 == 0:
            total += lst[i]
    return total if total != 0 else None