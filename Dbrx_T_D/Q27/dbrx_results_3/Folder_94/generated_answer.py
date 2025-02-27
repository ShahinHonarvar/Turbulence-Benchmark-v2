def insert_after_index(lst):
    index_to_insert = 74
    element_to_insert = 517.71
    new_index = index_to_insert + 1
    lst = lst[:new_index] + [element_to_insert] + lst[new_index:]
    return lst