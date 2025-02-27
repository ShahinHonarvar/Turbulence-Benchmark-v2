def insert_after_index(lst):
    if 89 in lst:
        index = lst.index(89) + 1
        lst.insert(index, 86)
    return lst