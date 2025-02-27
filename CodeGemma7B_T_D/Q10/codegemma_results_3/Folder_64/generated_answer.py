def all_odd_ints_exclusive(list_of_integers):
    if not any((x % 2 for x in list_of_integers)):
        return []
    return [x for x in list_of_integers if x % 2 and x >= 0 and (x < 5)]