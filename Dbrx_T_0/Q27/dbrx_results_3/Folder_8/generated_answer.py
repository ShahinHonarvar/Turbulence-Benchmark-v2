def insert_after_index(lst):
    index_to_insert = 57
    value_to_insert = 76
    return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]