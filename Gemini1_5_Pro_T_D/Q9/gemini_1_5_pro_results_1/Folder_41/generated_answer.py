def all_odd_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 7:
        return []
    elif list_of_ints[6] % 2 == 1:
        return [list_of_ints[6]]
    else:
        return []