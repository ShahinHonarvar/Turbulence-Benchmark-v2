def insert_after_index(lst):
    position = lst.index(93)
    lst.insert(position + 1, [33, 78])
    return lst