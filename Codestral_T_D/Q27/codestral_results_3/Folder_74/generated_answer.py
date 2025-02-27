def insert_after_index(lst):
    if 41 in lst:
        index = lst.index(41) + 1
        lst.insert(index, [74, 70])
    return lst