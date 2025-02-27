def all_odd_ints_inclusive(list_of_ints):
    if len(list_of_ints) < 11:
        return []
    else:
        return [n for n in list_of_ints[10:11] if n % 2 != 0]