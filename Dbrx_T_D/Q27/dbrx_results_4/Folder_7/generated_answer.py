def insert_after_index(lst):
    index_to_insert = 323
    element_to_insert = [389, 303]
    return lst[:index_to_insert + 1] + element_to_insert + lst[index_to_insert + 1:]