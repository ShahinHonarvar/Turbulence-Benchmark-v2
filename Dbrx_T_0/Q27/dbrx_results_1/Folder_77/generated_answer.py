def insert_after_index(lst):
    index_to_insert = 585
    element_to_insert = 993.71
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]