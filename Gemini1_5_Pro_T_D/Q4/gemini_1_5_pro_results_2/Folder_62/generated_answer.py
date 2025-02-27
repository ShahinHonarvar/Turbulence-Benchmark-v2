def all_pos_ints_exclusive(list_in):
    output = []
    for i in range(55, 84):
        try:
            if list_in[i] > 0:
                output.append(list_in[i])
        except:
            continue
    return output