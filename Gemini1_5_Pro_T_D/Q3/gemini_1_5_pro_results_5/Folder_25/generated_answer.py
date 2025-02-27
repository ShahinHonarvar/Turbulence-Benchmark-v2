def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(29, 94):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result