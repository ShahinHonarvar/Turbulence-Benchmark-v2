def all_pos_ints_inclusive(list_in):
    output = []
    for i in range(40, 81):
        if i >= len(list_in):
            break
        if list_in[i] > 0:
            output.append(list_in[i])
    return output