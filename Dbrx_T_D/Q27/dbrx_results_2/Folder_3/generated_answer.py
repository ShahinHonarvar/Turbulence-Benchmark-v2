def insert_after_index(lst):
    index_to_insert = 31
    element_to_insert = [88, 51]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]