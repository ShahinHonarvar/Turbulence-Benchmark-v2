def insert_after_index(lst):
    new_list = lst.copy()
    index_38 = new_list.index(38) if 38 in new_list else -1
    if index_38 != -1:
        new_list.insert(index_38 + 1, 45)
    return new_list