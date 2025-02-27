def insert_after_index(lst):
    index_to_insert = 87
    element_to_insert = 637.22
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]