def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(42, 69):
        if i % 2 != 0:
            if i < len(lst):
                total += lst[i]
    return total