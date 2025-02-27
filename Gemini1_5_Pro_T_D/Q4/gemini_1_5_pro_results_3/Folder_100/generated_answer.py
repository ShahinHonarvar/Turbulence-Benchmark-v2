def all_pos_ints_exclusive(list_of_integers):
    result = []
    for i in range(23, 24):
        if i >= 0 and i < len(list_of_integers) and (list_of_integers[i] > 0):
            result.append(list_of_integers[i])
    return result