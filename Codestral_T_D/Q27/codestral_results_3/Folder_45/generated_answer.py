def insert_after_index(lst):
    if 84 in lst:
        index = lst.index(84) + 1
        lst[index:index] = [[13, 46]]
    return lst