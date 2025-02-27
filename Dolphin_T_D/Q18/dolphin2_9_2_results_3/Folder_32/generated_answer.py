def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(25, 96):
        if lst[i] % 51 == 0 or lst[i] % 77 == 0:
            total += lst[i]
    return total if total != 0 else None