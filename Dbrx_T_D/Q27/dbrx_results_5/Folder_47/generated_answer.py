def insert_after_index(lst):
    index_to_insert = 64
    element_to_insert = 520.11
    if not lst:
        raise ValueError('List is empty')
    if len(lst) <= index_to_insert:
        raise ValueError('List does not have enough elements to insert after index 64')
    result = lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]
    return result