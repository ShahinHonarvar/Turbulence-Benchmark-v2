def insert_after_index(lst):
    index_60 = lst.index(60) if 60 in lst else None
    if index_60 is not None:
        lst.insert(index_60 + 1, 74)
        lst.insert(index_60 + 1, 80)
    return lst