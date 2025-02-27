def insert_after_index(lst):
    new_list = lst.copy()
    if 56 in new_list:
        index = new_list.index(56)
        new_list.insert(index + 1, 54)
    else:
        new_list.append(54)
    return new_list