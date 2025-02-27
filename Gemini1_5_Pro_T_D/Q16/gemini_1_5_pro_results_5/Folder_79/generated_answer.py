def sum_even_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 5:
        return 0
    if list_of_ints[4] % 2 == 0:
        return list_of_ints[4]
    else:
        return 0