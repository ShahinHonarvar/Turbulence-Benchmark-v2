def insert_after_index(lst):
    index = lst.index(52) if 52 in lst else -1
    if index != -1:
        lst.insert(index + 1, 38)
    return lst