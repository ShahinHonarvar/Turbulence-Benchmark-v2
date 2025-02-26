def insert_after_index(lst):
    if 62 in lst:
        insert_position = lst.index(62) + 1
        lst.insert(insert_position, 51)
    return lst