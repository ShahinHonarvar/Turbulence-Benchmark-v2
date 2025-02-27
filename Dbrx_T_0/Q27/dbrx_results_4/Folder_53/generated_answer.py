def insert_after_index(lst):
    index_to_insert = 92
    element_to_insert = 709.87
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]