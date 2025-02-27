def insert_after_index(lst):
    index_to_insert = lst.index(97) + 1
    return lst[:index_to_insert] + [47, 22] + lst[index_to_insert:]