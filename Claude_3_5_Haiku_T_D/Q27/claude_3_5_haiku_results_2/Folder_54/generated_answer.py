def insert_after_index(lst):
    if 43 in lst:
        insert_position = lst.index(43) + 1
        lst.insert(insert_position, 37)
    return lst