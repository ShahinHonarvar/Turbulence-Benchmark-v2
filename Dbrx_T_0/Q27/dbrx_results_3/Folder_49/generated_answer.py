def insert_after_index(lst):
    index_to_insert = 38
    element_to_insert = [27, 34]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]