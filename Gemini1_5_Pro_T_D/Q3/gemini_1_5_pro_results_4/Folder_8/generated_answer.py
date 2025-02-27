def all_pos_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 24:
        return []
    sublist = list_of_integers[23:24]
    result = []
    for i in sublist:
        if i > 0:
            result.append(i)
    return result