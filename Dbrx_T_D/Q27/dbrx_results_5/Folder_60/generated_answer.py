def insert_after_index(lst):
    index_to_insert = 21
    value_to_insert = 74
    return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]