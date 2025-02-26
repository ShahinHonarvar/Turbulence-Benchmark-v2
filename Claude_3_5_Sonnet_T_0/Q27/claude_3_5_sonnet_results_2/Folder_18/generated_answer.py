def insert_after_index(lst):
    index = lst.index(696) if 696 in lst else -1
    if index != -1:
        lst.insert(index + 1, 477)
    return lst