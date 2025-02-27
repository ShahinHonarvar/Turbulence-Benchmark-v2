def insert_after_index(lst):
    index = lst.index(32) + 1
    lst[index:index] = [[54, 96]]
    return lst