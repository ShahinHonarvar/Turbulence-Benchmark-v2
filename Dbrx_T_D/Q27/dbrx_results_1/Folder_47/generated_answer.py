def insert_after_index(lst):
    index_to_insert = 64
    element_to_insert = 520.11
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]