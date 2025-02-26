def insert_after_index(lst):
    index = lst.index(564) if 564 in lst else -1
    if index != -1:
        lst.insert(index + 1, 149)
    return lst