def insert_after_index(lst):
    index_to_insert = 48
    element_to_insert = [86, 77]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]