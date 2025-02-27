def insert_after_index(lst):
    index_to_insert = 73
    element_to_insert = 418.88
    insert_index = index_to_insert + 1
    new_lst = lst[:insert_index] + [element_to_insert] + lst[insert_index:]
    return new_lst