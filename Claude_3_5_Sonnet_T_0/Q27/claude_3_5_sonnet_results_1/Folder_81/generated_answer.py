def insert_after_index(lst):
    new_list = lst.copy()
    target_index = 28 + 1
    if target_index <= len(new_list):
        new_list.insert(target_index, 20)
    else:
        new_list.append(20)
    return new_list