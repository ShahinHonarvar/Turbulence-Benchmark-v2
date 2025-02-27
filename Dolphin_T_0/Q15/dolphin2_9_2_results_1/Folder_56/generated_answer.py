def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(0, 1):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum