def insert_after_index(lst):
    index_to_insert = 24
    element_to_insert = [98, 22]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]