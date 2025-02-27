def insert_after_index(lst):
    index_to_insert = 295
    element_to_insert = [276, 376]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]