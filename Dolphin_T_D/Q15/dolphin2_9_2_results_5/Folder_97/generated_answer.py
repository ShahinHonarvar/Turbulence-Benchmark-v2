def sum_odd_ints_inclusive(lst):
    result = 0
    for i in range(40, 81):
        if lst[i] % 2 == 1:
            result += lst[i]
    return result if result != 0 else 0