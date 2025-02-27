def sum_odd_ints_inclusive(lst):
    start = 661
    end = 924
    total = 0
    if start < 0 or end > len(lst) - 1 or start > end:
        return 0
    for i in range(start, end + 1):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total