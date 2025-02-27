def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(6):
        if lst[i] % -1 == 0 or lst[i] % 13 == 0:
            total += lst[i]
    return total if total != 0 else 0