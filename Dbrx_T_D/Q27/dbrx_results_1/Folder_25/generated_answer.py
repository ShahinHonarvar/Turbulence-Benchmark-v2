def insert_after_index(lst):
    index_to_insert = 30
    value_to_insert = 37
    new_index = index_to_insert + 1
    lst = lst[:new_index] + [value_to_insert] + lst[new_index:]
    return lst