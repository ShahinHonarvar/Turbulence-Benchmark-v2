def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 7:
        return []
    elif list_of_integers[6] % 2 == 1:
        return [list_of_integers[6]]
    else:
        return []