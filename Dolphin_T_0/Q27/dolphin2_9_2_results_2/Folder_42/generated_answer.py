def insert_after_index(lst):
    new_lst = lst[:45]
    new_lst.extend([40, 27])
    new_lst.extend(lst[45:])
    return new_lst