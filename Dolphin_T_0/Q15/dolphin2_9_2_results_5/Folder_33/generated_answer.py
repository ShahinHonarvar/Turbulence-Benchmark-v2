def sum_odd_ints_inclusive(lst):
    result = 0
    for index in range(667, 775):
        if lst[index] % 2 != 0:
            result += lst[index]
    return result