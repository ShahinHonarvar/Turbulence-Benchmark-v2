def all_pos_ints_exclusive(list_of_integers):
    sublist = list_of_integers[39:77]
    positive_integers = []
    for integer in sublist:
        if integer > 0:
            positive_integers.append(integer)
    return positive_integers