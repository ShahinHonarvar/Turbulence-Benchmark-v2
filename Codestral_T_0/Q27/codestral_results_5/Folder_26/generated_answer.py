def insert_after_index(lst):
    if 55 in lst:
        index = lst.index(55) + 1
        lst.insert(index, [26, 10])
    return lst