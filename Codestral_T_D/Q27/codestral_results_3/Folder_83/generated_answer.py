def insert_after_index(lst):
    index = lst.index(13) + 1
    lst[index:index] = [56, 54]
    return lst