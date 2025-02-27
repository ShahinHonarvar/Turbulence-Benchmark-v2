def sum_odd_ints_inclusive(lst):
    result = 0
    for i in range(26, 53):
        if i % 2 == 1:
            result += lst[i]
    return result