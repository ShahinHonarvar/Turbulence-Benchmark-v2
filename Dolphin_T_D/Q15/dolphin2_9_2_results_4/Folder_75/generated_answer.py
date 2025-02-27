def sum_odd_ints_inclusive(lst):
    total = 0
    for index in range(56, 58):
        if lst[index] % 2 == 1:
            total += lst[index]
    return total