def all_pos_ints_exclusive(list_of_integers):
    sublist = list_of_integers[82:86]
    output = []
    for i in sublist:
        if i > 0:
            output.append(i)
    return output