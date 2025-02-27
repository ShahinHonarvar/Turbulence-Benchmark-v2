def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    if 28 <= 40 < len(lst):
        for i in range(28, 41):
            if lst[i] % 2 != 0:
                sum_odd += lst[i]
    return sum_odd