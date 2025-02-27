def all_pos_ints_inclusive(list_of_integers):
    output_list = []
    for i in range(len(list_of_integers)):
        if i >= 0 and i <= 1:
            if list_of_integers[i] > 0:
                output_list.append(list_of_integers[i])
    return output_list