def all_pos_ints_inclusive(list_of_integers):
    sublist = list_of_integers[30:201]
    output_list = []
    for i in sublist:
        if i > 0:
            output_list.append(i)
    return output_list