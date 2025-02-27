def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(5):
        if lst[i] % 8 == 0 or lst[i] % -3 == 0:
            total += lst[i]
    return total if total != 0 else None