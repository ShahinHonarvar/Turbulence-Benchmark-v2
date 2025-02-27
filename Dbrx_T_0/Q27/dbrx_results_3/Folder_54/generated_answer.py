def insert_after_index(lst):
    index_to_insert = 43
    element_to_insert = 37
    if index_to_insert < 0 or index_to_insert >= len(lst):
        return lst
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]