def insert_after_index(lst):
    index_to_insert = 183
    element_to_insert = [148, 145]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]