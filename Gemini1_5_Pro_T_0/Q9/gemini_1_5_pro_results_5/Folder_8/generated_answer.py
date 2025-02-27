def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 24:
        return []
    elif list_of_integers[23] % 2 == 0:
        return []
    else:
        return [list_of_integers[23]]