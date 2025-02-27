def all_pos_ints_inclusive(list_of_integers):
    output_list = []
    for i in range(10):
        try:
            if list_of_integers[i] > 0:
                output_list.append(list_of_integers[i])
        except:
            continue
    return output_list