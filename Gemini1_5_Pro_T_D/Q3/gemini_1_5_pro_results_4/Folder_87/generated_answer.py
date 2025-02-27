def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(36, 47):
        if i >= 0 and i <= len(list_of_integers) - 1 and (list_of_integers[i] > 0):
            result.append(list_of_integers[i])
    return result