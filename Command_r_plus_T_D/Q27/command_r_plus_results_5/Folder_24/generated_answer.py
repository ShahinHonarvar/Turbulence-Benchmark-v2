def insert_after_index(lst):
    index = lst.index(42)
    lst.insert(index + 1, 53)
    return lst