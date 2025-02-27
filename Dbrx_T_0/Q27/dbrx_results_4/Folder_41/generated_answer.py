def insert_after_index(lst):
    index_to_insert = lst.index(87) + 1
    lst.insert(index_to_insert, [78, 16])
    return lst