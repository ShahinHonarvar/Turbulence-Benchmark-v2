def insert_after_index(lst):
    new_list = lst.copy()
    index_44 = 44 if 44 < len(new_list) else -1
    new_list.insert(index_44 + 1, 76)
    return new_list