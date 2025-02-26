def insert_after_index(lst):
    new_list = lst.copy()
    insert_index = 58 if len(lst) > 58 else len(lst)
    new_list.insert(insert_index, 76)
    return new_list