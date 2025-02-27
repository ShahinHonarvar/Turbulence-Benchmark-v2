def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(28, 33):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total if total else 0