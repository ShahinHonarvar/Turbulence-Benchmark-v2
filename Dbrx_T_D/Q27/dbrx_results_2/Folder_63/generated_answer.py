def insert_after_index(lst):
    index_to_insert = 76
    data_to_insert = [15, 51]
    return lst[:index_to_insert + 1] + data_to_insert + lst[index_to_insert + 1:]