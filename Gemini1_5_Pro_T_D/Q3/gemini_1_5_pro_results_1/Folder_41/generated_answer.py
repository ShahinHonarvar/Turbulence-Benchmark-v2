def all_pos_ints_inclusive(list_of_integers):
    result = []
    if len(list_of_integers) > 6 and list_of_integers[6] > 0:
        result.append(list_of_integers[6])
    return result