def insert_after_index(lst):
    index = lst.index(693) if 693 in lst else -1
    if index != -1:
        lst.insert(index + 1, 606)
        lst.insert(index + 2, 873)
    return lst