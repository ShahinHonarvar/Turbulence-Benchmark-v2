def insert_after_index(lst):
    if 90 in lst:
        insert_position = lst.index(90) + 1
        lst.insert(insert_position, 80)
    return lst