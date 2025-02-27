def insert_after_index(lst):
    index_to_insert = 21
    element_to_insert = 74
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]