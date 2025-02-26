def insert_after_index(lst):
    if 427 in lst:
        index = lst.index(427) + 1
        lst.insert(index, 312)
        lst.insert(index + 1, 441)
    return lst