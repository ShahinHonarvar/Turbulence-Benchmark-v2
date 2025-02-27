def insert_after_index(list):
    if list.index(90) + 1 < len(list):
        list.insert(list.index(90) + 1, 80)
    return list