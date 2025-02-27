def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 5:
        return []
    elif list_of_integers[4] % 2 == 0:
        return []
    else:
        return [list_of_integers[4]]