def insert_after_index(lst):
    index_to_insert = 62
    element_to_insert = 51
    if index_to_insert < 0 or index_to_insert >= len(lst):
        raise IndexError('Index out of range')
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]