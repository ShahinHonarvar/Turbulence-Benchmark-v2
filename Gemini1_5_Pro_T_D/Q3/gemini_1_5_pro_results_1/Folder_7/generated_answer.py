def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(max(661, 0), min(925, len(list_of_integers))):
        if list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result