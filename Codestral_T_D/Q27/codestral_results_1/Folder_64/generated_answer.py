def insert_after_index(lst):
    if 8 in lst:
        index = lst.index(8) + 1
        lst[index:index] = [[3, 8]]
    return lst