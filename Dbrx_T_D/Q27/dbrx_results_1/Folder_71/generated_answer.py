def insert_after_index(lst):
    index_to_insert = 70
    to_insert = 76
    return lst[:index_to_insert + 1] + [to_insert] + lst[index_to_insert + 1:]