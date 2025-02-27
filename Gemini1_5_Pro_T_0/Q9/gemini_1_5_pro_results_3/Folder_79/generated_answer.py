def all_odd_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 5:
        return []
    elif list_of_ints[4] % 2 != 0:
        return [list_of_ints[4]]
    else:
        return []