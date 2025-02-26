def insert_after_index(lst):
    index_69 = lst.index(69) if 69 in lst else -1
    if index_69 != -1:
        lst.insert(index_69 + 1, 92)
    return lst