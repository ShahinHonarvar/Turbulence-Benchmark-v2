def all_pos_ints_inclusive(list_of_integers):
    result = []
    if len(list_of_integers) > 0:
        for integer in list_of_integers[:1]:
            if integer > 0:
                result.append(integer)
    return result