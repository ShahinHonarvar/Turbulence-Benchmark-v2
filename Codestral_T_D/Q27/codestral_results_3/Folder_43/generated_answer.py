def insert_after_index(lst):
    if 29 < len(lst) - 1:
        lst.insert(lst.index(29) + 1, [28, 53])
    return lst