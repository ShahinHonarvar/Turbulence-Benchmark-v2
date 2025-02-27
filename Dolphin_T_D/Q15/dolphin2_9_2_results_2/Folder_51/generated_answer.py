def sum_odd_ints_inclusive(list_of_ints):
    sum_odd = 0
    for i in range(1, 9):
        if list_of_ints[i] % 2 != 0:
            sum_odd += list_of_ints[i]
    return sum_odd