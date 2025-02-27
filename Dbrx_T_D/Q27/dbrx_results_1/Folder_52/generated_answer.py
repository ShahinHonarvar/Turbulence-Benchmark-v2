def insert_after_index(lst):
    index_to_insert = 97
    value_to_insert = 72.27
    if index_to_insert < len(lst) - 1:
        lst.insert(index_to_insert + 1, value_to_insert)
    return lst