def insert_after_index(lst):
    index_to_insert = 53
    element_to_insert = 783.25
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]