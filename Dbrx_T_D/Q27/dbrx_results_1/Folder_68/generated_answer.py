def insert_after_index(lst):
    index_to_insert = 8
    element_to_insert = [1, 7]
    return lst[:index_to_insert] + element_to_insert + lst[index_to_insert:]