def insert_after_index(lst):
    if 36 in lst:
        index = lst.index(36) + 1
        lst[index:index] = [[54, 13]]
    return lst