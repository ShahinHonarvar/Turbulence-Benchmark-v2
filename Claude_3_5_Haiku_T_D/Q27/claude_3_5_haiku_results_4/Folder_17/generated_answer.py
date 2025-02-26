def insert_after_index(lst):
    if 94 in lst:
        insert_position = lst.index(94) + 1
        lst.insert(insert_position, 93)
    return lst