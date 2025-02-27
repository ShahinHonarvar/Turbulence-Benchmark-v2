def insert_after_index(lst):
    index_to_insert = 100
    element_to_insert = [876, 203]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]