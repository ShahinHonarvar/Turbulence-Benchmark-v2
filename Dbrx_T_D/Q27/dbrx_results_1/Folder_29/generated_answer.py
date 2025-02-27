def insert_after_index(lst):
    index_to_insert = 96
    if index_to_insert > len(lst) - 1:
        lst.append(36)
    else:
        lst.insert(index_to_insert + 1, 36)
    return lst