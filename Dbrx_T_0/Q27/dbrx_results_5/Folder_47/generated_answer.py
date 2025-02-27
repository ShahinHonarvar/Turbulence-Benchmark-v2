def insert_after_index(lst):
    index_to_insert = 64
    element_to_insert = 520.11
    if index_to_insert < 0 or index_to_insert >= len(lst):
        return lst
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]