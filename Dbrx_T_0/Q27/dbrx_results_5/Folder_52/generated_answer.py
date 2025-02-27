def insert_after_index(lst):
    index_to_insert = 97
    value_to_insert = 72.27
    new_lst = lst[:]
    new_lst.insert(index_to_insert + 1, value_to_insert)
    return new_lst