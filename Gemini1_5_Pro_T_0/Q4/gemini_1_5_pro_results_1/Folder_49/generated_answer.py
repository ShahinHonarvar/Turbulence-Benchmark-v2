def all_pos_ints_exclusive(list_of_integers):
    sub_list = list_of_integers[80:200]
    output_list = []
    for integer in sub_list:
        if integer > 0:
            output_list.append(integer)
    return output_list