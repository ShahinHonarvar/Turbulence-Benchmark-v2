def insert_after_index(lst):
    index = lst.index(44) + 1
    lst.insert(index, 40)
    lst.insert(index + 1, 27)
    return lst