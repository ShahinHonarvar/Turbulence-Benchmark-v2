def insert_after_index(lst):
    index_to_insert = 62
    number_to_insert = 51
    if index_to_insert >= len(lst):
        return lst
    return lst[:index_to_insert + 1] + [number_to_insert] + lst[index_to_insert + 1:]