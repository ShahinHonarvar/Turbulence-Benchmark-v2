def all_pos_ints_exclusive(list_of_integers):
    result = []
    for i in range(1, min(9, len(list_of_integers))):
        if list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result