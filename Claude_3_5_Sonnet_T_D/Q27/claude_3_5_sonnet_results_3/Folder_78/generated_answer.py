def insert_after_index(lst):
    index_to_insert = lst.index(63) + 1 if 63 in lst else 0
    lst.insert(index_to_insert, 99)
    return lst