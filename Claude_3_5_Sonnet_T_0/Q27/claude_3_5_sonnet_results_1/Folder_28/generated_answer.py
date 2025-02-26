def insert_after_index(lst):
    new_list = lst.copy()
    target_index = 74
    if target_index < len(new_list):
        new_list.insert(target_index + 1, 49)
    else:
        new_list.append(49)
    return new_list