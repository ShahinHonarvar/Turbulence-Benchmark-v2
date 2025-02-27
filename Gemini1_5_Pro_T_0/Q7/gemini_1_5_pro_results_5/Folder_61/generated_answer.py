def all_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 8:
        return []
    elif list_of_integers[7] % 2 == 0:
        return [list_of_integers[7]]
    else:
        return []