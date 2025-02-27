def insert_after_index(lst):
    index_to_insert = 55
    element_to_insert = [26, 10]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]