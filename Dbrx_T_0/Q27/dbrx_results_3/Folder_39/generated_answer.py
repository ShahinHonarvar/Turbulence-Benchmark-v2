def insert_after_index(lst):
    index_to_insert = 97
    element_to_insert = [47, 22]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]