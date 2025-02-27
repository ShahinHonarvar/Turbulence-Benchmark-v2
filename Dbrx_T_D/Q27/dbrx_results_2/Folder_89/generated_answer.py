def insert_after_index(lst):
    index_to_insert = 62 + 1
    element_to_insert = 51
    return lst[:index_to_insert] + [element_to_insert] + lst[index_to_insert:]