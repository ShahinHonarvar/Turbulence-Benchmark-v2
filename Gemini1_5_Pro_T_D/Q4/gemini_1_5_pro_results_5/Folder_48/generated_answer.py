def all_pos_ints_exclusive(list_of_integers):
    sublist = list_of_integers[386:999]
    positive_integer_list = []
    for integer in sublist:
        if integer > 0:
            positive_integer_list.append(integer)
    return positive_integer_list