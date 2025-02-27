def insert_after_index(lst):
    index = 99
    if index < len(lst):
        lst.insert(index + 1, 99)
    return lst