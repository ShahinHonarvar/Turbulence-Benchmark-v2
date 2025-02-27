def sum_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 7:
        return 0
    if list_of_integers[6] % 2 == 0:
        return 0
    else:
        return list_of_integers[6]