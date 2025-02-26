def insert_after_index(lst):
    if 99 in lst:
        insert_pos = lst.index(99) + 1
        lst.insert(insert_pos, 99)
    return lst