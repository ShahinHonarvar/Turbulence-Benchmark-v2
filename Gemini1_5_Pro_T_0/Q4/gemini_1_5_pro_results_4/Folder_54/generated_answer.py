def all_pos_ints_exclusive(list_of_integers):
    sublist = list_of_integers[27:34]
    output_list = []
    for i in sublist:
        if i > 0:
            output_list.append(i)
    return output_list