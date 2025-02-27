def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(1, 5):
        if lst[i] % 4 == 0 or lst[i] % -6 == 0:
            total += lst[i]
    return total if total != 0 else 0