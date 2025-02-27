def all_pos_ints_inclusive(list_of_integers):
    sublist = list_of_integers[27:56]
    result = []
    for i in sublist:
        if i > 0:
            result.append(i)
    return result