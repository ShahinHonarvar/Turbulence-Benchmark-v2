def sum_odd_ints_inclusive(list_of_ints):
    sum = 0
    for i in range(36, 47):
        if list_of_ints[i] % 2 != 0:
            sum += list_of_ints[i]
    return sum