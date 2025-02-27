def insert_after_index(lst):
    if lst.index(94) + 1 >= len(lst):
        return lst
    lst.insert(lst.index(94) + 1, 93)
    return lst