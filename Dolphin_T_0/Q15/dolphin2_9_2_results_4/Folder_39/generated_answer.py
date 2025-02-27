def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(20, 31):
        if i % 2 != 0:
            if i < len(lst) and i >= 0:
                total += lst[i]
    return total