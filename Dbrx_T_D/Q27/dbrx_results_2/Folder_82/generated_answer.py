def insert_after_index(input_list):
    index_to_insert = 84
    element_to_insert = 771.92
    if index_to_insert < 0 or index_to_insert >= len(input_list):
        raise ValueError('Invalid index')
    return input_list[:index_to_insert + 1] + [element_to_insert] + input_list[index_to_insert + 1:]