def all_pos_ints_inclusive(list_of_integers):
    output_list = []
    for i in range(64, 67):
        if i in range(len(list_of_integers)) and list_of_integers[i] > 0:
            output_list.append(list_of_integers[i])
    return output_list