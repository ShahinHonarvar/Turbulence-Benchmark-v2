def all_even_ints_inclusive(list_in):
    output_list = []
    for i in range(0, 2):
        if i < len(list_in):
            if list_in[i] % 2 == 0:
                output_list.append(list_in[i])
    return output_list