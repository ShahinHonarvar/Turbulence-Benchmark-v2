def insert_after_index(lst):
    index_to_insert = 500
    element_to_insert = [912, 170]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]