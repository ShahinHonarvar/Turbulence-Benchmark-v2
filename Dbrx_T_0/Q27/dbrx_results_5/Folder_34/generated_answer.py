def insert_after_index(lst):
    index_to_insert = 53
    if index_to_insert < len(lst) - 1:
        index_to_insert += 1
    else:
        index_to_insert = len(lst)
    lst.insert(index_to_insert, 783.25)
    return lst