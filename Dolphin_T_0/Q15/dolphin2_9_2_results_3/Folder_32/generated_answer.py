def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(21, 98):
        total += lst[i] if lst[i] % 2 != 0 else 0
    return total