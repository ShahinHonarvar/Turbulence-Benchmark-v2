def insert_after_index(lst):
    if 99 in lst:
        index_99 = lst.index(99)
        lst.insert(index_99 + 1, 15)
    else:
        lst.append(15)
    return lst