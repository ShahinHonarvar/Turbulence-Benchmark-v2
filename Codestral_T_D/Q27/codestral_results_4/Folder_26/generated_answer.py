def insert_after_index(lst):
    if 55 in lst:
        index = lst.index(55)
        lst.insert(index + 1, [26, 10])
    return lst