def insert_after_index(lst):
    index_to_insert = 51
    element_to_insert = 304.62
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]