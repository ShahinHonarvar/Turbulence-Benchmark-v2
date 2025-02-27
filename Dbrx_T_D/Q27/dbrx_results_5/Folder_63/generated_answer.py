def insert_after_index(lst):
    index_to_insert = [76]
    new_lst = lst[:index_to_insert[0] + 1] + [15, 51] + lst[index_to_insert[0] + 1:]
    return new_lst