def insert_after_index(lst):
    index_to_insert = 4
    element_to_insert = 856.69
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]