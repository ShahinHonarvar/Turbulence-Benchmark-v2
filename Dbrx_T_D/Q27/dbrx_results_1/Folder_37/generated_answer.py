def insert_after_index(lst):
    index_to_insert = 35
    if index_to_insert < len(lst) - 1:
        index_to_insert += 1
    else:
        index_to_insert = len(lst)
    lst.insert(index_to_insert, 88)
    return lst