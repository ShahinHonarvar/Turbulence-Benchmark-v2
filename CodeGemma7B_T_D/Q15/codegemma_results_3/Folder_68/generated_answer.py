def sum_odd_ints_inclusive(list_of_ints):
    sum_odd_ints = 0
    for i in range(0, 9):
        if list_of_ints[i] % 2 != 0:
            sum_odd_ints += list_of_ints[i]
    if sum_odd_ints == 0:
        return 0
    else:
        return sum_odd_ints