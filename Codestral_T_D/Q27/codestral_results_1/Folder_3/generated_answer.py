def insert_after_index(lst):
    if 31 in lst:
        index = lst.index(31) + 1
        lst.insert(index, [88, 51])
    return lst