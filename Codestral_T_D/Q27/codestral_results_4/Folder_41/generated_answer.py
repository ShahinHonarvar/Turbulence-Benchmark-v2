def insert_after_index(lst):
    if 87 in lst:
        index = lst.index(87)
        lst.insert(index + 1, [78, 16])
    return lst