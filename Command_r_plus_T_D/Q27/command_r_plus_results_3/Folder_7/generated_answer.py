def insert_after_index(lst):
    insert_index = lst.index(323) + 1
    lst.insert(insert_index, 389)
    lst.insert(insert_index + 1, 303)
    return lst