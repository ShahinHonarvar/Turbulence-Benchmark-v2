def insert_after_index(list_in):
    list_out = list_in.copy()
    list_out.insert(list_in.index(87) + 1, [78, 16])
    return list_out