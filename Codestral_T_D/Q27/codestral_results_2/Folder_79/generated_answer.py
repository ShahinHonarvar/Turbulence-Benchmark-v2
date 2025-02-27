def insert_after_index(lst):
    if 28 in lst:
        index = lst.index(28) + 1
        lst.insert(index, [41, 69])
    return lst