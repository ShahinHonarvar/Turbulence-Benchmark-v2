def sum_ints_div_by_either_nums(lst):
    total = 0
    for idx in range(32, 100):
        if lst[idx] % -11 == 0 or lst[idx] % -15 == 0:
            total += lst[idx]
    return total if total != 0 else 0