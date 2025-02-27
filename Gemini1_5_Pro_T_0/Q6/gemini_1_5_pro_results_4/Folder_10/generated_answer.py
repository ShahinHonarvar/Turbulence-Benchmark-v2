def all_neg_ints_exclusive(list_in):
    out_list = []
    for i in range(48, 74):
        if i < len(list_in) and list_in[i] < 0:
            out_list.append(list_in[i])
    return out_list