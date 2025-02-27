def insert_after_index(lst):
    index_to_insert = 166
    value_to_insert = 232
    if index_to_insert >= len(lst):
        return lst + [value_to_insert]
    return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]