def all_odd_ints_inclusive(list_of_integers):
    if not any((x % 2 for x in list_of_integers[1:6])):
        return []
    return [x for x in list_of_integers[1:6] if x % 2]