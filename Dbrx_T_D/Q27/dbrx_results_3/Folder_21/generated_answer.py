def insert_after_index(lst):
    index_to_insert = 743
    element_to_insert = 11.04
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]