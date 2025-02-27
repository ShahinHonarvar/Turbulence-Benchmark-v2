def insert_after_index(lst):
    index_to_insert = 76
    element_to_insert = [15, 51]
    insert_index = index_to_insert + 1
    lst = lst[:insert_index] + element_to_insert + lst[insert_index:]
    return lst