def insert_after_index(list_in):
    i = list_in.index(983)
    return list_in[0:i + 1] + [369] + list_in[i + 1:]