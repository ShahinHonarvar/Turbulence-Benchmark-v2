def insert_after_index(lst):
    index = lst.index(29) if 29 in lst else -1
    if index != -1:
        lst.insert(index + 1, [28, 53])
    return lst