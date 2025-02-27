def all_pos_ints_inclusive(list_of_integers):
    result = []
    for i in range(list_of_integers[0], list_of_integers[1] + 1):
        if i > 0:
            result.append(i)
    return result