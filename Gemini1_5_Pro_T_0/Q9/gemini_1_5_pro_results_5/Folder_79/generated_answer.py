def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 5:
        return []
    if list_of_integers[4] % 2 == 1:
        return [list_of_integers[4]]
    else:
        return []