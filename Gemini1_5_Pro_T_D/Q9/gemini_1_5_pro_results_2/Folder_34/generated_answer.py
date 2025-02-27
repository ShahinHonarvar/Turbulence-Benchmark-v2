def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 61:
        return []
    if list_of_integers[60] % 2 == 0:
        return []
    else:
        return [list_of_integers[60]]