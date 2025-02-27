def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(246, 751):
        if i % 2 != 0:
            total += i
    return total if total != 0 else 0