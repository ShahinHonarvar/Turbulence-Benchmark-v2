def insert_after_index(lst):
    index_85 = lst.index(85) if 85 in lst else -1
    if index_85 != -1:
        lst.insert(index_85 + 1, [41, 95])
    return lst