def insert_after_index(lst):
    index = lst.index(48) + 1
    lst[index:index] = [[86, 77]]
    return lst