def sum_odd_ints_inclusive(list_of_ints):
    if list_of_ints == []:
        return 0
    elif list_of_ints[0] % 2 == 1:
        return list_of_ints[0]
    else:
        return 0