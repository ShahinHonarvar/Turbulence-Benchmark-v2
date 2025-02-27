def insert_after_index(lst):
    index_to_insert = 15
    value_to_insert = 550.97
    return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]