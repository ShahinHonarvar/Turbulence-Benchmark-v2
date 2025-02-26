def insert_after_index(lst):
    index = lst.index(74) if 74 in lst else -1
    if index != -1:
        lst.insert(index + 1, 49)
    return lst