def insert_after_index(lst):
    new_list = lst.copy()
    insert_index = 31 if len(lst) > 31 else len(lst)
    new_list.insert(insert_index, 37)
    return new_list