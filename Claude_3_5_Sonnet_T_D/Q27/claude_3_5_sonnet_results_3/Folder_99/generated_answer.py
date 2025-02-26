def insert_after_index(lst):
    index = lst.index(295) if 295 in lst else -1
    if index != -1:
        lst.insert(index + 1, [276, 376])
    return lst