def all_even_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 8:
        return []
    elif list_of_ints[7] % 2 == 0:
        return [list_of_ints[7]]
    else:
        return []