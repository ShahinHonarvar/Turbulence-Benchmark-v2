def all_pos_ints_exclusive(list_of_integers):
    sublist = list_of_integers[51:200]
    output_list = []
    for element in sublist:
        if element > 0:
            output_list.append(element)
    return output_list