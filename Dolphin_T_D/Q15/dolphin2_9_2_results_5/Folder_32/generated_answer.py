def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(21, 98):
        if i in lst and i % 2 != 0:
            total += i
    return total if total != 0 else None