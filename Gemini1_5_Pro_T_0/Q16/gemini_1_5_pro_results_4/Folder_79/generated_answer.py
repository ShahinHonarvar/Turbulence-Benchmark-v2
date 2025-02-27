def sum_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 5:
        return 0
    if list_of_integers[4] % 2 == 0:
        return list_of_integers[4]
    else:
        return 0