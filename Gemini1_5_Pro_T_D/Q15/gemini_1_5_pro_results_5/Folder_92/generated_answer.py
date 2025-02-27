def sum_odd_ints_inclusive(list_of_ints):
    if len(list_of_ints) > 1:
        if list_of_ints[1] % 2 != 0:
            return list_of_ints[1]
    return 0