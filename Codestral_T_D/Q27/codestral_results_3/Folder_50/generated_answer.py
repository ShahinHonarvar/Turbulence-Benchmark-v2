def insert_after_index(lst):
    if 52 in lst:
        index_52 = lst.index(52)
        lst.insert(index_52 + 1, 38)
    return lst