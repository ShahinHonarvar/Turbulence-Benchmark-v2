def insert_after_index(lst):
    index = lst.index(76) + 1
    lst[index:index] = [[15, 51]]
    return lst