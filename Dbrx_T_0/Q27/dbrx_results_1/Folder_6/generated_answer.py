def insert_after_index(lst):
    index_to_insert = 86
    value_to_insert = 581.49
    return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]