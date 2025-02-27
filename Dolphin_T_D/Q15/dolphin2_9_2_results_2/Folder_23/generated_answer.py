def sum_odd_ints_inclusive(list_of_ints):
    total = 0
    for i in range(52, 72):
        if list_of_ints[i] % 2 != 0:
            total += list_of_ints[i]
    return total