def insert_after_index(lst):
    index_to_insert = lst.index(74) + 1
    lst = lst[:index_to_insert] + [49] + lst[index_to_insert:]
    return lst