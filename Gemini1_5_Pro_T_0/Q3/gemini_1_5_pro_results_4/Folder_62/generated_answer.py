def all_pos_ints_inclusive(list_of_integers):
    sublist = list_of_integers[91:100]
    output_list = []
    for integer in sublist:
        if integer > 0:
            output_list.append(integer)
    return output_list