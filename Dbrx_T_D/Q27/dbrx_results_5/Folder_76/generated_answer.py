def insert_after_index(lst):
    index_to_insert = 166
    value_to_insert = 232
    return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]