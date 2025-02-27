def insert_after_index(lst):
    index_to_insert = 15
    value_to_insert = 550.97
    new_lst = lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]
    return new_lst