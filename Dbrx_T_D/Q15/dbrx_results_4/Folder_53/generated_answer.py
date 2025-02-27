def sum_odd_ints_inclusive(lst):
    start = 300
    end = 300
    total = 0
    for i in range(start, end + 1):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total if total > 0 else 0