def insert_after_index(lst):
    if 21 in lst:
        index = lst.index(21) + 1
        lst.insert(index, [83, 14])
    return lst