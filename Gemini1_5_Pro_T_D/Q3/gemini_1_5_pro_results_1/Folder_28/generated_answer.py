def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(62, 64):
        if i >= len(list_of_integers) or list_of_integers[i] <= 0:
            continue
        result.append(list_of_integers[i])
    return result