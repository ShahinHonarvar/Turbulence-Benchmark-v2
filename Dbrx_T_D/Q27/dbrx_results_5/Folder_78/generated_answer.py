def insert_after_index(lst):
    index_to_insert = lst.index(63) + 1
    lst.insert(index_to_insert, 99)
    return lst