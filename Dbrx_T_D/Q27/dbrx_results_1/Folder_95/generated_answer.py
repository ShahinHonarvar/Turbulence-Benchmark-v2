def insert_after_index(lst):
    index_to_insert = 20 + 1
    lst = lst[:index_to_insert] + [80] + lst[index_to_insert:]
    return lst