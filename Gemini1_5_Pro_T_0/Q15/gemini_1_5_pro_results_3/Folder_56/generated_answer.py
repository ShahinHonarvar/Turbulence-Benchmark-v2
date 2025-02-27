def sum_odd_ints_inclusive(list_of_ints):
    if len(list_of_ints) == 0:
        return 0
    elif list_of_ints[0] % 2 == 0:
        return 0
    else:
        return list_of_ints[0]