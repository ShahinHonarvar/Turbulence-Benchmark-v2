def insert_after_index(lst):
    new_lst = lst[:41]
    new_lst.extend([74, 70])
    new_lst.extend(lst[41:])
    return new_lst