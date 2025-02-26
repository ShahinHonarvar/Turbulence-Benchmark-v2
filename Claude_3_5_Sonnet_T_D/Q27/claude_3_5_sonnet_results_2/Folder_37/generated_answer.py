def insert_after_index(lst):
    new_list = lst.copy()
    if len(new_list) > 35:
        new_list.insert(36, 88)
    else:
        new_list.append(88)
    return new_list