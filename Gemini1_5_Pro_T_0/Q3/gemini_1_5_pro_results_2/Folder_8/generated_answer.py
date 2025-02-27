def all_pos_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 24:
        return []
    sublist = list_of_integers[23:24]
    output = []
    for element in sublist:
        if element > 0:
            output.append(element)
    return output