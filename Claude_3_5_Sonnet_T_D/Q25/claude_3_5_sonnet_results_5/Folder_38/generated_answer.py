def insert_at_index(lst):
    new_list = lst.copy()
    if len(new_list) >= 89:
        new_list.insert(89, 86)
    else:
        new_list.extend([None] * (89 - len(new_list)) + [86])
    return new_list