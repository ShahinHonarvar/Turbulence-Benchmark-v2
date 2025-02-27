def sum_odd_ints_inclusive(lst):
    result = 0
    for i in range(5, 8):
        if lst[i] % 2 != 0:
            result += lst[i]
    return result