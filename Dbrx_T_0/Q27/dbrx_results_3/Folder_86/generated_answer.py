def insert_after_index(lst):
    index_to_insert = 990
    element_to_insert = [905, 742]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]