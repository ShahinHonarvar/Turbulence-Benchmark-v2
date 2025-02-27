def insert_after_index(lst):
    if 29 in lst:
        index = lst.index(29) + 1
        lst[index:index] = [[28, 53]]
    return lst