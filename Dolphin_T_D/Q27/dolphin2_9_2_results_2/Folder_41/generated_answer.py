def insert_after_index(lst):
    index_position = lst.index(87)
    if index_position != -1:
        lst.insert(index_position + 1, [78, 16])
    else:
        lst.append([78, 16])
    return lst