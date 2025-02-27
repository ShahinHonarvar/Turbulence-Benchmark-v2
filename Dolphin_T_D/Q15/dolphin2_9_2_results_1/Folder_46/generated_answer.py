def sum_odd_ints_inclusive(lst):
    sum = 0
    if 30 < len(lst):
        for i in range(30, 88):
            if lst[i] % 2 != 0:
                sum += lst[i]
    return sum