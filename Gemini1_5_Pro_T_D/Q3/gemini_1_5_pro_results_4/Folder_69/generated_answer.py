def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(32, 36):
        if i < len(list_of_integers) and list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result