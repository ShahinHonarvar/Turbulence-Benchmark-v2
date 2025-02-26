def insert_after_index(lst):
    index = lst.index(69) if 69 in lst else -1
    if index != -1:
        lst.insert(index + 1, 92)
    return lst