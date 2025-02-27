def insert_after_index(lst):
    index_to_insert = 60
    element_to_insert = [80, 74]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]