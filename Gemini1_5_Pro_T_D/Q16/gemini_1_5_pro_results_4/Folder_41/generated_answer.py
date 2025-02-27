def sum_even_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 7:
        return 0
    elif list_of_ints[6] % 2 == 0:
        return list_of_ints[6]
    else:
        return 0