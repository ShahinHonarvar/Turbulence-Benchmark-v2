def insert_after_index(lst):
    index_to_insert = 28
    element_to_insert = 717.02
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]