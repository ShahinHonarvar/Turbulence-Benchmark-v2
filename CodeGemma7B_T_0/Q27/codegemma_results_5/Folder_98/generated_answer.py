def insert_after_index(list):
    if list.index(9) + 1 < len(list):
        list.insert(list.index(9) + 1, 1)
    return list