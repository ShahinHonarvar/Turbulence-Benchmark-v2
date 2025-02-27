def insert_after_index(list):
    item = list.pop(43)
    list.insert(44, 37)
    list.insert(44, item)
    return list