def insert_after_index(lst):
    index_to_insert = 69
    element_to_insert = 92
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]