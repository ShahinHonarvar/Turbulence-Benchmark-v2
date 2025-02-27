def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(max(0, min(62, len(list_of_integers))), min(64, len(list_of_integers))):
        if list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result