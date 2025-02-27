def all_pos_ints_exclusive(list_of_integers):
    sub_list = list_of_integers[3:8]
    positive_integer_list = []
    for integer in sub_list:
        if integer > 0:
            positive_integer_list.append(integer)
    return positive_integer_list