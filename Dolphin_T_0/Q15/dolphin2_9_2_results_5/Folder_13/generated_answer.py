def sum_odd_ints_inclusive(lst):
    total = 0
    for index in range(25, 88):
        if lst[index] % 2 != 0:
            total += lst[index]
    return total if total != 0 else 0