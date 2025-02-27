def insert_after_index(lst):
    index_to_insert = 427
    element_to_insert = [312, 441]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]