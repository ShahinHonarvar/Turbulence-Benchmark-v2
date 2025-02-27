def insert_after_index(lst):
    if 89 in lst:
        idx = lst.index(89)
        lst.insert(idx + 1, 86)
    return lst