def insert_after_index(lst):
    if 85 in lst:
        index = lst.index(85) + 1
        lst.insert(index, [41, 95])
    return lst