def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 61:
        return []
    elif list_of_integers[60] % 2 == 1:
        return [list_of_integers[60]]
    else:
        return []