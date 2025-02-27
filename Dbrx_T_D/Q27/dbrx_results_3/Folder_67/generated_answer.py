def insert_after_index(lst):
    index_to_insert = 44
    element_to_insert = 76
    if index_to_insert >= len(lst):
        return lst
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]