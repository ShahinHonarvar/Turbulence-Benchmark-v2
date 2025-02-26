def insert_after_index(lst):
    new_list = lst.copy()
    index_to_insert = lst.index(166) + 1
    new_list.insert(index_to_insert, 232)
    return new_list