def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(10):
        if lst[i] % 10 == 0 or lst[i] % 100 == 0:
            total += lst[i]
    return total if total != 0 else None