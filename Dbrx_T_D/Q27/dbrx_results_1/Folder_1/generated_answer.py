def insert_after_index(lst):
    index_to_insert = 93
    element_to_insert = [33, 78]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]