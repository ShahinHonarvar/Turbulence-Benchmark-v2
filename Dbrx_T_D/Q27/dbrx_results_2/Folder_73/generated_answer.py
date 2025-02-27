def insert_after_index(lst):
    index_to_insert = 87
    new_element = 637.22
    return lst[:index_to_insert + 1] + [new_element] + lst[index_to_insert + 1:]