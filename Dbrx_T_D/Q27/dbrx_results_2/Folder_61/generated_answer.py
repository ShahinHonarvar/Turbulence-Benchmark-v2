def insert_after_index(lst):
    index = 4
    while index < len(lst):
        lst.insert(index + 1, 7)
        index += 1
    return lst