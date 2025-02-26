def insert_after_index(lst):
    if 323 in lst:
        index = lst.index(323) + 1
        lst.insert(index, 389)
        lst.insert(index + 1, 303)
    return lst