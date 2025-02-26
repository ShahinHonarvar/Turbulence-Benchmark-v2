def insert_after_index(lst):
    new_list = lst.copy()
    target_index = 166
    if target_index < len(new_list):
        new_list.insert(target_index + 1, 232)
    else:
        new_list.append(232)
    return new_list