def sum_odd_ints_inclusive(list_ints):
    total = 0
    for i in range(13, 69):
        if list_ints[i] % 2 != 0:
            total += list_ints[i]
    return total