def insert_after_index(lst):
    if 30 in lst:
        index_30 = lst.index(30)
        lst.insert(index_30 + 1, 37)
    else:
        lst.append(37)
    return lst