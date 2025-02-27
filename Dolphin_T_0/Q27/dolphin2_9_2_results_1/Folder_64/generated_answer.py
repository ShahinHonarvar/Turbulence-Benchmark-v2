def insert_after_index(lst):
    new_list = lst[:9]
    new_list.extend([3, 8])
    new_list.extend(lst[9:])
    return new_list