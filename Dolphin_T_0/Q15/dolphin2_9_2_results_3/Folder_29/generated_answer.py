def sum_odd_ints_inclusive(lst):
    total = 0
    for index in range(59, 98):
        if lst[index] % 2 == 1:
            total += lst[index]
    return total if total != 0 else 0