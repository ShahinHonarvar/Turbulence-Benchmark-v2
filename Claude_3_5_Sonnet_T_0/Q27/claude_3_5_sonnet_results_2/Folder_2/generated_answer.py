def insert_after_index(lst):
    index = lst.index(427) if 427 in lst else -1
    if index != -1:
        lst.insert(index + 1, 312)
        lst.insert(index + 2, 441)
    return lst