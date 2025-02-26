def insert_after_index(lst):
    new_list = lst.copy()
    target_index = 63
    if target_index < len(new_list):
        new_list.insert(target_index + 1, 99)
    else:
        new_list.append(99)
    return new_list