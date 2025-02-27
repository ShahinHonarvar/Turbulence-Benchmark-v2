def insert_after_index(lst):
    index_to_insert = 52
    while index_to_insert + 1 not in lst or list[index_to_insert + 1] != 38:
        index_to_insert += 1
    lst.insert(index_to_insert + 1, 38)
    return lst