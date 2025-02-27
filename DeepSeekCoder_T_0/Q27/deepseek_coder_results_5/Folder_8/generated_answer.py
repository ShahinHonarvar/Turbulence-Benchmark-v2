def insert_after_index(lst):
    if 57 in lst:
        index_57 = lst.index(57)
        lst.insert(index_57 + 1, 76)
    else:
        lst.append(76)
    return lst