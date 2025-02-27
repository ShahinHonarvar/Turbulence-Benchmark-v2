def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(40, 81):
        total += lst[i] if lst[i] % 2 != 0 else 0
    return total