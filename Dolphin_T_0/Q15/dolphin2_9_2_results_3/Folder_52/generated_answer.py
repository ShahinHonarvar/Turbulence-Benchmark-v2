def sum_odd_ints_inclusive(lst):
    if len(lst) < 28:
        return 0
    total = 0
    for i in range(28, 39):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total if total != 0 else None