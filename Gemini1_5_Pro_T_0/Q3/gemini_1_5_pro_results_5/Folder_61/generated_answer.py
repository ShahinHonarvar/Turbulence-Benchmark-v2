def all_pos_ints_inclusive(list_of_integers):
    output_list = []
    for i in range(min(len(list_of_integers), 8)):
        if list_of_integers[i] > 0:
            output_list.append(list_of_integers[i])
    return output_list