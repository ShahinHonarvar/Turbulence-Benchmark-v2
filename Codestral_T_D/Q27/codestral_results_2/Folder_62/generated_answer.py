def insert_after_index(lst):
    index_to_insert = lst.index(35) + 1
    lst.insert(index_to_insert, [90, 76])
    return lst