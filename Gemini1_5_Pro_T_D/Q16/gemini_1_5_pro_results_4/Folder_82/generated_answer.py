def sum_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 30:
        return 0
    elif list_of_integers[29] % 2 == 0:
        return list_of_integers[29]
    else:
        return 0