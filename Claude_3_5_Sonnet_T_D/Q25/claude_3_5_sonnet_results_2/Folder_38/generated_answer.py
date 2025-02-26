def insert_at_index(lst):
    new_list = lst.copy()
    if len(new_list) <= 89:
        new_list.extend([None] * (90 - len(new_list)))
    new_list.insert(89, 86)
    return new_list