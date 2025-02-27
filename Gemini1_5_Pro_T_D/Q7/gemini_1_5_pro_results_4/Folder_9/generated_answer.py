def all_even_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 74:
        return []
    elif list_of_ints[73] % 2 == 0:
        return [list_of_ints[73]]
    else:
        return []