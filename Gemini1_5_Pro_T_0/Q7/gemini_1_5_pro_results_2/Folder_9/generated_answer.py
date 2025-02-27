def all_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 74:
        return []
    if list_of_integers[73] % 2 == 0:
        return [list_of_integers[73]]
    else:
        return []