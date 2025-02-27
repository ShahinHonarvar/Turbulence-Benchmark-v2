def insert_after_index(lst):
    index_to_insert = 21 + 1
    new_list = lst[:index_to_insert] + [74] + lst[index_to_insert:]
    return new_list