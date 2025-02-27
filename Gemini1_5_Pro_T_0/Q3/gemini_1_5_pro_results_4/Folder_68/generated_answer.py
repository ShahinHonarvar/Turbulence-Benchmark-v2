def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(min(9, len(list_of_integers))):
        if list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result