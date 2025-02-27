def sum_odd_ints_inclusive(list_of_ints):
    sum_odd_ints = 0
    for i in range(40, 81):
        if list_of_ints[i] % 2 != 0:
            sum_odd_ints += list_of_ints[i]
    return sum_odd_ints if sum_odd_ints != 0 else 0