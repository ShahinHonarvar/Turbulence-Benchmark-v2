def all_odd_ints_inclusive(list_of_integers):
    if len(list_of_integers) > 60:
        return [number for number in list_of_integers[60:61] if number % 2 != 0]
    else:
        return []