def insert_after_index(lst):
    index_to_insert = 84
    element_to_insert = 771.92
    new_lst = lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]
    return new_lst