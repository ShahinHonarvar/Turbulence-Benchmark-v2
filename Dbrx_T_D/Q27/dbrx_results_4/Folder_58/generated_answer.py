def insert_after_index(lst):
    index_to_insert = 598
    element_to_insert = [385, 999]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]