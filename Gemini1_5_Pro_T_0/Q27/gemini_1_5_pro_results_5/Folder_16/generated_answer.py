def insert_after_index(list_in):
    list_out = []
    for i in range(len(list_in)):
        list_out.append(list_in[i])
        if i == 983:
            list_out.append(369)
    return list_out