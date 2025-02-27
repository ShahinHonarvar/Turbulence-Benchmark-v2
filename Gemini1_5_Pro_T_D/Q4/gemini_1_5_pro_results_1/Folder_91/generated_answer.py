def all_pos_ints_exclusive(list_of_integers):
    result = []
    for i in range(1, 5):
        if list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result