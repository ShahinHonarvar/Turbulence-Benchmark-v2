def insert_after_index(lst):
    index_to_insert = 693
    element_to_insert = [606, 873]
    if index_to_insert < 0 or index_to_insert >= len(lst):
        raise ValueError('Index out of range')
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]