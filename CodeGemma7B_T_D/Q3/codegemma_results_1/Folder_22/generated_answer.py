def all_pos_ints_inclusive(my_list):
    output_list = []
    for i in range(40, 201):
        if my_list[i] > 0:
            output_list.append(my_list[i])
    return output_list