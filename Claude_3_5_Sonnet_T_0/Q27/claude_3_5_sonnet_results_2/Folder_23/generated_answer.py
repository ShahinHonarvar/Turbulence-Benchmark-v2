def insert_after_index(lst):
    new_list = lst.copy()
    index_to_insert = lst.index(38) + 1
    new_list.insert(index_to_insert, 45)
    return new_list