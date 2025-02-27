def insert_after_index(lst):
    if 43 in lst:
        index = lst.index(43) + 1
        lst.insert(index, 37)
    return lst