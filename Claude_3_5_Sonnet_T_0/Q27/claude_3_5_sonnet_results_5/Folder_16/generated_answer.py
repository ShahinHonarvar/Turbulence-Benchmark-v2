def insert_after_index(lst):
    index = lst.index(983) if 983 in lst else -1
    if index != -1:
        lst.insert(index + 1, 369)
    return lst