def insert_after_index(lst):
    if 89 not in lst:
        return lst
    index = lst.index(89)
    lst.insert(index + 1, 86)
    return lst