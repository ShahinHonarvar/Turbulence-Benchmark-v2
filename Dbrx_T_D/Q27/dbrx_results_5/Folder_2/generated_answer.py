def insert_after_index(lst):
    index_to_insert = 427
    element_to_insert = [312, 441]
    if index_to_insert < 0 or index_to_insert > len(lst) - 1:
        raise ValueError('Index is out of range')
    return lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]